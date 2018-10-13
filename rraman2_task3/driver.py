## Author : Ragavi Swarnalatha Raman (rraman2) - 200203611 ##
#!/usr/bin/python
import sys
import random
import math
import itertools
import functools
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
CLS = float(args[1])
CLR = 5.0
b_size = int(args[2])
seed = int(args[3])
random.seed(seed)

##arrays to store T and D values
arr_T = []
arr_D = []
mean_T = []
mean_D = []
percentile_T = []
percentile_D = []

i=1
no_batches = 0
fd = open("./output.txt",'w+')

def percentile(arr): ##function to calculate the 95th percentile
    k = (len(arr)-1) * 0.95
    f = math.floor(k)
    c = math.ceil(k)
    if f == c:
        return arr[int(k)]
    x0 = arr[int(f)] * (c-k)
    x1 = arr[int(c)] * (k-f)
    return x0+x1

simul_obj = Simulation(mc,cla,buffer,cls,clr) ## Calling Simulation
while no_batches <= max_batches:
	fd.write("Batch No:"+str(no_batches)+"\n")
	fd.write("Requestid"+"				"+"T"+"									"+"D"+"\n")
	while i <= max_obsv:
		id,T,D = simul_obj.simulation(CLA,CLS,CLR,b_size,seed,i)
		if T != 0:
			fd.write(str(id)+"				"+str(T)+"									"+str(D)+"\n")
			arr_T.append(T)
			arr_D.append(D)
		i+=1
	##calculate mean for T and D at the end of each batch
	arr_T = sorted(arr_T)
	arr_D = sorted(arr_D)
	##calculating mean and 95th percentile for each batch
	mean_T.append(sum(arr_T)/len(arr_T))
	mean_D.append(sum(arr_D)/len(arr_D))
	percentile_T.append(percentile(arr_T))
	percentile_D.append(percentile(arr_D))
	arr_T = []
	arr_D = []
	i = 1 
	no_batches+=1

##Print statements to file
j = 1
fd.write("\n"+"means for each batch:"+"\n")
for (x,y) in itertools.izip(mean_T,mean_D):
	fd.write(str(j)+"                              "+str(x)+"                                                                      "+str(y)+"\n")
	j += 1

j = 1
fd.write("\n"+"95th percentile for each batch:"+"\n")
for (x,y) in itertools.izip(percentile_T,percentile_D):
	fd.write(str(j)+"                              "+str(x)+"                                                                      "+str(y)+"\n")
	j += 1

##Calculating super mean for mean and 95th percentile
mean_T.pop(0)
mean_D.pop(0)
percentile_T.pop(0)
percentile_D.pop(0)

super_T_mean = sum(mean_T) / len(mean_T)
super_D_mean = sum(mean_D) / len(mean_D)
percentile_T_mean = sum(percentile_T) / len(percentile_D)
percentile_D_mean = sum(percentile_D) / len(percentile_D)
stnd_dev_mean_T = math.sqrt(sum(pow(x - super_T_mean,2) for x in mean_T) / len(mean_T))
stnd_dev_mean_D = math.sqrt(sum(pow(x - super_D_mean,2) for x in mean_D) / len(mean_D))
stnd_dev_percentile_T = math.sqrt(sum(pow(x - percentile_T_mean,2) for x in percentile_T) / len(percentile_T))
stnd_dev_percentile_D = math.sqrt(sum(pow(x - percentile_D_mean,2) for x in percentile_D) / len(percentile_D))

fd.write("super mean,standard deviation of T"+"\n")
fd.write(str(super_T_mean)+","+str(stnd_dev_mean_T)+"\n")

fd.write("super mean,standard deviation of D"+"\n")
fd.write(str(super_D_mean)+","+str(stnd_dev_mean_D)+"\n")

fd.write("mean,standard deviation of 95th percentile of T"+"\n")
fd.write(str(percentile_T_mean)+","+str(stnd_dev_percentile_T)+"\n")

fd.write("mean,standard deviation of 95th percentile of D"+"\n")
fd.write(str(percentile_D_mean)+","+str(stnd_dev_percentile_D)+"\n")

##calculating the confidence intervals for T and D values
mean_ci_t_a = super_T_mean + (1.96 * (stnd_dev_mean_T/math.sqrt(50)))
mean_ci_t_b = super_T_mean - (1.96 * (stnd_dev_mean_T/math.sqrt(50)))

mean_ci_d_a = super_D_mean + (1.96 * (stnd_dev_mean_D/math.sqrt(50)))
mean_ci_d_b = super_D_mean - (1.96 * (stnd_dev_mean_D/math.sqrt(50)))

percent_ci_t_a = percentile_T_mean + (1.96 * (stnd_dev_percentile_T/math.sqrt(50)))
percent_ci_t_b = percentile_T_mean - (1.96 * (stnd_dev_percentile_T/math.sqrt(50)))

percent_ci_d_a = percentile_D_mean + (1.96 * (stnd_dev_percentile_D/math.sqrt(50)))
percent_ci_d_b = percentile_D_mean - (1.96 * (stnd_dev_percentile_D/math.sqrt(50)))

fd.write("Confidence Intervals of Mean of T"+"\n")
fd.write(str(mean_ci_t_a)+","+str(mean_ci_t_b)+"\n")

fd.write("Confidence Intervals of Mean of D"+"\n")
fd.write(str(mean_ci_d_a)+","+str(mean_ci_d_b)+"\n")

fd.write("Confidence Intervals of Percentile of T"+"\n")
fd.write(str(percent_ci_t_a)+","+str(percent_ci_t_b)+"\n")

fd.write("Confidence Intervals of Percentile of D"+"\n")
fd.write(str(percent_ci_d_a)+","+str(percent_ci_d_b)+"\n")

fd.close()
 
