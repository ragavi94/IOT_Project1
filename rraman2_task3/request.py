## Author : Ragavi Swarnalatha Raman (rraman2) - 200203611 ##

class Request:
	##initializing request values
	def __init__(self,arrival,trans_delay,buffer_time,completion):
		self.arrival = arrival
		self.trans_delay = trans_delay
		self.buffer_time = buffer_time
		self.completion = completion

	##update values on a new arrival
	def update_req(self,timer,clck_str):
		if clck_str == "CLS":
			self.completion = timer
			print("request completion time changed to:",self.completion)
		
		if clck_str == "CLR":
			self.trans_delay = self.arrival
			self.buffer_time = timer
			print("request trans_delay and buffer time after changes:",self.trans_delay,self.buffer_time)

	##service completion - calculate T,D values and return them
	def getdata(self):
		T = self.completion - self.arrival
		D = self.buffer_time - self.trans_delay
		return T,D
		
