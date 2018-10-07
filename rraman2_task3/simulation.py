## Author : Ragavi Swarnalatha Raman (rraman2) - 200203611 ##
import random
from request import Request
class Simulation:
	## initializing default values
	def __init__(self,mc,cla,buffer,cls,clr):
		self.req_hash = {}
		self.mc = mc
		self.cla = cla
		self.buffer = buffer
		self.cls = cls
		self.lastid = 0
		self.clr = []
		if len(clr) != 0:
			self.clr.extend(clr)

	##Calculate next exponential arrival time
	def calc_next_arrival(self,lambda_CLA):
		return random.expovariate(1/lambda_CLA)

	##Calculate the next orbiting/retransmission completion time
	def calc_next_orbit(self,lambda_CLR):
		return random.expovariate(1/lambda_CLR)

	##Form request object and add to hash_map
	def new_request(self,id):
		self.req_hash[id] = Request(self.mc,0,0,0)
		print(self.req_hash)
		return id

	##Get Hash map records and individual request's buffer values after a retransmission/orbiting time
	def get_req_buffer(self):
		id = min([k for k,v in self.req_hash.items() if v.buffer_time == self.mc])
		return id

	##Update Hash map records and individual request's timer values after a retransmission/orbiting time
	def update_hashmap_CLR(self,id,timer,clck_str):
		if id in self.req_hash.keys():
			req = self.req_hash[id]
			req.update_req(timer,clck_str)
			self.req_hash[id] = req
		

	##Update Hash map records and individual request's timer values on a new arrival
	def update_hashmap_CLA(self,id,timer,clck_str):
		if id in self.req_hash.keys():
			req = self.req_hash[id]
			req.update_req(timer,clck_str)
			self.req_hash[id] = req
	
	##Update Hash map records and individual request's timer values, find T and D values on a service completion
	def update_hashmap_CLS(self,T,D):
		tmp = [v.completion for v in self.req_hash.values()]
		print("hashtable:",tmp)
		id_list = [ k for k,v in self.req_hash.items() if (v.completion != 0 and v.completion == self.cls)]
		print("removing id from hashmap:",id_list)
		if id_list == []:
			print("hash table:")
			print("aborting")
			exit()
		for key in id_list:
			req = self.req_hash[key]
			T,D = req.getdata()
			del self.req_hash[key]
		return id_list,T,D
	
	##find next master clock value
	def find_min(self):
		clck_str = []
		tmp_list = []
		tmp_list.append(self.cla)
		if not (self.buffer == 0 and self.mc > 0):
			tmp_list.append(self.cls)
		if len(self.clr) > 0:
			tmp_list.append(self.clr[0])
		if self.mc == 0 and len(self.clr) == 0: ##first entry
			next_mc = self.cla
		else:
			next_mc = min(tmp_list)
		if next_mc == self.cla:
			clck_str.append("CLA")
		if next_mc == self.cls:
			clck_str.append("CLS")
		if len(self.clr) != 0 and next_mc == self.clr[0]:
			clck_str.append("CLR")
		return next_mc,clck_str

	##Actual Simulation Logic
	def simulation(self,CLA,CLS,CLR,b_size,seed,i):
		print("i:",i)
		print("CLA:",self.cla)
		print("MC:",self.mc)		
		T=0
		D=0
		next_mc,clck_str = self.find_min()
		self.mc = next_mc

		print("Advancing MC to "+str(self.mc))
		if "CLR" in clck_str: ##Priority1: CLR. Add to buffer if buffer limit is not reached.Else append back to Retransmission queue with new wait completion value
			print("CLR entry after orbiting")
			i_list = [i for i in range(0,len(self.clr)) if self.mc == self.clr[i]]
			for i in i_list:
				self.clr.pop(0)	
				if self.buffer == b_size:
					next_CLR = self.calc_next_orbit(CLR) ##Generated random variable
                        		print("next_CLR"+str(self.mc)+" "+str(next_CLR))
					sum = self.mc + next_CLR
					id = self.get_req_buffer()
					print("id of  the request that has come after reorbiting:",id)
					self.update_hashmap_CLR(id,sum,"CLR")
					self.clr.append(sum)
					self.clr = sorted(self.clr)
				elif self.buffer < b_size:
                                        id = self.get_req_buffer()
                                        print("id of  the request that has come after reorbiting:",id)
					self.buffer += 1
					if self.buffer == 1:
						self.update_hashmap_CLR(id,self.mc + CLS,"CLS")
						self.cls = self.mc + CLS
					elif self.buffer > 1:
						self.update_hashmap_CLR(id,self.cls + ((self.buffer-1)*CLS),"CLS")

		if "CLA" in clck_str: ##Priority2: CLA. Add to buffer if buffer limit is not reached.Else append to Retransmission queue with new wait completion value
			print("new arrival entry,ID number:",self.lastid+1)
			self.lastid += 1
			self.new_request(self.lastid)
			next_CLA = self.calc_next_arrival(CLA) ##Generated random variable
			print("next_CLA:"+str(self.mc)+" "+str(next_CLA)+"\n")
			self.cla += next_CLA
			if self.buffer == b_size:
				next_CLR = self.calc_next_orbit(CLR) ##Generated random variable
				print("full buffer:"+" "+str(self.mc)+" "+str(next_CLR)+"\n")
				sum = self.mc + next_CLR
				self.update_hashmap_CLA(self.lastid,sum,"CLR")
				self.clr.append(sum)
				self.clr = sorted(self.clr)
			elif self.buffer < b_size:
				self.buffer += 1
				if self.buffer == 1:
					self.update_hashmap_CLA(self.lastid,self.mc + CLS,"CLS")
					self.cls = self.mc + CLS
				elif self.buffer > 1:
					self.update_hashmap_CLA(self.lastid,self.cls + ((self.buffer-1)*CLS),"CLS")
				
					
		if "CLS" in clck_str: ##Priority3: CLS. Remove 1 entry from buffer to indicate sending next waiting request in buffer for execution. Replace with new service completion time
			print("service completion entry") 
			self.buffer -= 1
			id,T,D = self.update_hashmap_CLS(T,D)
			if self.buffer > 0:
				self.cls += CLS
			print("id:",id,"T:",T,"D:",D)
			print('MC:'+str(self.mc)+" "+'CLA:'+str(self.cla)+" "+'Buffer:'+str(self.buffer)+" "+'CLS:'+str(self.cls)+" "+'CLR:'+str(self.clr)+'\n\n')
			return id,T,D				
		print('MC:'+str(self.mc)+" "+'CLA:'+str(self.cla)+" "+'Buffer:'+str(self.buffer)+" "+'CLS:'+str(self.cls)+" "+'CLR:'+str(self.clr)+'\n\n')		
		return 0,0,0
		

