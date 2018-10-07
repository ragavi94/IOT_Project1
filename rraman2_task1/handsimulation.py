## Author : Ragavi Swarnalatha Raman (rraman2) - 200203611 ##
class Simulation:
	## initializing default values
	def __init__(self,mc,cla,buffer,cls,clr):
		self.mc = mc
		self.cla = cla
		self.buffer = buffer
		self.cls = cls
		self.clr = []
		if len(clr) != 0:
			self.clr.extend(clr)

	##To find the next master clock value
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
	
	##Actual simulation logic
	def simulation(self,CLA,CLS,CLR,b_size,fd):
		fd.write("finding next min value to advance MC"+'\n')
		next_mc,clck_str = self.find_min()
		self.mc = next_mc
		
		fd.write("Advancing MC to "+str(self.mc)+'\n')
		if "CLR" in clck_str: ##Priority1: CLR. Add to buffer if buffer limit is not reached.Else append back to Retransmission queue with new wait completion value
			fd.write("CLR entry after orbiting"+'\n')
			i_list = [i for i in range(0,len(self.clr)) if self.mc == self.clr[i]]
			for i in i_list:
				self.clr.pop(0)	
				if self.buffer == b_size:
					sum = self.mc + CLR
					self.clr.append(sum)
				elif self.buffer < b_size:
					self.buffer += 1
		if "CLA" in clck_str: ##Priority2: CLA. Add to buffer if buffer limit is not reached.Else append to Retransmission queue with new wait completion value
			fd.write("new arrival entry"+'\n')
			self.cla += CLA
			if self.buffer == b_size:
				sum = self.mc + CLR
				self.clr.append(sum)
			elif self.buffer < b_size:
				self.buffer += 1
				if self.buffer == 1:
					self.cls = self.mc + CLS
				
		if "CLS" in clck_str: ##Priority3: CLS. Remove 1 entry from buffer to indicate sending next waiting request in buffer for execution. Replace with new service completion time
			fd.write("service completion entry"+'\n') 
			self.buffer -= 1
			if self.buffer > 0:
				self.cls += CLS

		
		fd.write('MC:'+str(self.mc)+" "+'CLA:'+str(self.cla)+" "+'Buffer:'+str(self.buffer)+" "+'CLS:'+str(self.cls)+" "+'CLR:'+str(self.clr)+'\n\n')
		return self.mc,self.cla,self.buffer,self.cls,self.clr
