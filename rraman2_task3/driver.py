## Author : Ragavi Swarnalatha Raman (rraman2) - 200203611 ##
#!/usr/bin/python
import sys
import random
import itertools
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

max_obsv = 1000
max_batches = 50

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
mean_T = []
mean_D = []

i=1
no_batches = 0
fd = open("./output.txt",'w+')

simul_obj = Simulation(mc,cla,buffer,cls,clr) ## Calling Simulation
while no_batches <= max_batches:
	fd.write("Batch No:"+str(no_batches)+"\n")
	while i <= max_obsv:
		id,T,D = simul_obj.simulation(CLA,CLS,CLR,b_size,seed,i)
		if T != 0:
			fd.write(str(id)+"				"+str(T)+"									"+str(D)+"\n")
			arr_T.append(T)
			arr_D.append(D)
		i+=1
	##calculate mean for T and D at the end of each batch
	fd.write("sum_T:"+str(sum(arr_T)))
	fd.write("sum_D:"+str(sum(arr_D)))
	fd.write(str(len(arr_T)))
	fd.write(str(len(arr_D)))
	mean_T.append(sum(arr_T)/len(arr_T))
	mean_D.append(sum(arr_D)/len(arr_D))
	arr_T = []
	arr_D = []
	i = 1 
	no_batches+=1

j = 1
fd.write("\n"+"means for each batch:"+"\n")
for (x,y) in itertools.izip(mean_T,mean_D):
	fd.write(str(j)+"                              "+str(x)+"                                                                      "+str(y)+"\n")
	j += 1

mean_T.pop(0)
mean_D.pop(0)
super_T_mean = sum(mean_T) / len(mean_T)
super_D_mean = sum(mean_D) / len(mean_D)
fd.write("super mean T and D"+"\n")
fd.write(str(j)+"                              "+str(super_T_mean)+"                                                                      "+str(super_D_mean)+"\n")

fd.close()
 
