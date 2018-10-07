Language : Python2.7
Platform : Ubuntu 16.04 / remote.eos.ncsu.edu
Usage: driver.py <inter-arrival-time> <mean-orbiting-time> <service-time> <buffer-size> <mc-termination-value> <seed>

Assumptions:
1.	The first arrival comes at MC = 2
2.	The mean new arrival value is 6 seconds, CLA = 6
	The exponential variable is generated using random.seed(seed) initially and then random.expovariate(1/6.0) [equivalent to -1/lambda log(1-r)]
3.	The service completion time for each request is 10 seconds, CLS = 10
4.	The mean orbiting time value is, CLR = 5
	The exponential variable is generated using random.seed(seed) initially and then random.expovariate(1/5.0) [equivalent to -1/lambda log(1-r)]
5.	Order of Preference when multiple events occur at the same MC:
	a.	Retransmitted Request
	b.	New Request
	c.	Service Completion
6.	Maxinum MC value = 200

(1) The driver.py contains the default values from the assumptions made. ie) first entry 0 2 0 - - 
(2) driver.py calls the simulation() funtion under the handsimulation.py file
(3) Simulation values per iteration are returned back to driver.py and printed in output.txt 



