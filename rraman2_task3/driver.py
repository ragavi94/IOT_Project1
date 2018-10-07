## Author : Ragavi Swarnalatha Raman (rraman2) - 200203611 ##
#!/usr/bin/python
import sys
import random
#sys.path.append("./task1/")
from simulation import Simulation

args = sys.argv
if len(args) != 4:
	print("Usage: driver.py <service-time> <buffer-size> <seed>")
	exit(1)	

## inputs and defaults
mc = 0
buffer = 0
cla = 2
cls = 0
clr = []

max_obsv = 100
max_batches = 3

## arrival,completion and orbiting times
CLA = 6.0
CLS = int(args[1])
CLR = 5.0
b_size = int(args[2])
seed = int(args[3])
random.seed(seed)

##arrays to store T and D values
arr_T = []
arr_D = []

i=1
no_batches = 0
fd = open("./output.txt",'w+')

simul_obj = Simulation(mc,cla,buffer,cls,clr) ## Calling Simulation
while no_batches < max_batches:
	fd.write("Batch No:"+str(no_batches)+"\n")
	while i <= max_obsv:
		id,T,D = simul_obj.simulation(CLA,CLS,CLR,b_size,seed)
		if T != 0:
			fd.write(str(id)+"		"+str(T)+"							"+str(D)+"\n")
		arr_T.append(T)
		arr_D.append(D)
		i+=1
	i = 1 
	no_batches+=1

fd.close()
 
