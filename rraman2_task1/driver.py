## Author : Ragavi Swarnalatha Raman (rraman2) - 200203611 ##
#!/usr/bin/python
import sys
#sys.path.append("./task1/")
from handsimulation import Simulation

args = sys.argv
if len(args) != 6:
	print("Usage: driver.py <inter-arrival-time> <mean-orbiting-time> <service-time> <buffer-size> <mc-termination-value>")
	exit(1)	

## inputs and defaults
mc = 0
cla = 2
buffer = 0
cls = 0
clr = []

max_mc = int(args[5]) ## maximum Master Clock Value
simulation_table = []

## arrival,completion and orbiting times
CLA = int(args[1])
CLS = int(args[3])
CLR = int(args[2])
b_size = int(args[4])

i=0
fd = open("./output.txt",'w+')

simul_obj = Simulation(mc,cla,buffer,cls,clr) ## Calling Simulation
simulation_table.append(['MC', 'CLA', 'Buffer', 'CLS', 'CLR'])
simulation_table.append([str(mc),str(cla),str(buffer),str(cls),str(clr)])
while i <= max_mc:
	mc,cla,buffer,cls,clr = simul_obj.simulation(CLA,CLS,CLR,b_size,fd)
	simulation_table.append([str(mc),str(cla),str(buffer),str(cls),str(clr)])
	i = mc

fd.write("Consolidated Simulation Output Table"+'\n\n\n')
for item in simulation_table:
#	print("          	".join(item))
	fd.write("	                 ".join(item)+"\n")

print("Generating Output in output.txt. Do 'cat output.txt'")
fd.close()
 
