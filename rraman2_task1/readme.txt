Language : Python2.7
Platform : Ubuntu 16.04 / remote.eos.ncsu.edu
Usage: driver.py <inter-arrival-time> <mean-orbiting-time> <service-time> <buffer-size> <mc-termination-value>

Assumptions:
1.	The first arrival comes at MC = 2
2.	A new arrival comes every 6 seconds, CLA = 6
3.	The service completion time for each request is 10 seconds, CLS = 10
4.	Each retransmitted request waits for 5 seconds, CLR = 5
5.	Order of Preference when multiple events occur at the same MC:
	a.	Retransmitted Request
	b.	New Request
	c.	Service Completion
6.	Maxinum MC value = 200

(1) The driver.py contains the default values from the assumptions made. ie) first entry 0 2 0 - - 
(2) driver.py calls the simulation() funtion under the handsimulation.py file
(3) Simulation values per iteration are returned back to driver.py and printed in output.txt 





