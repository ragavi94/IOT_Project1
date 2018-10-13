Language : Python2.7
Platform : Ubuntu 16.04 / remote.eos.ncsu.edu
Usage: driver.py <service-time> <buffer-size> <seed>

Example: driver.py 5 5 5 > output1.txt

(Please redirect all print statements to a file as shown above during running to avoid slow execution and unwanted print statements)

Assumptions:
1.	The first arrival comes at MC = 2
2.	The mean new arrival value is 6 seconds, CLA = 6
	The exponential variable is generated using random.seed(seed) initially and then random.expovariate(1/6.0) [equivalent to -1/lambda log(1-r)]
3.	The mean orbiting time value is, CLR = 5
	The exponential variable is generated using random.seed(seed) initially and then random.expovariate(1/5.0) [equivalent to -1/lambda log(1-r)]
4.	Order of Preference when multiple events occur at the same MC:
	a.	Retransmitted Request
	b.	New Request
	c.	Service Completion
5.	Number of Batches = 50
6.	Maxinum number of observations per batch = 1000
7.	All mean and super mean values are calculated as [sum of values/total number of values]
8.	Standard Deviation = sqrt(summation((ith value - mean)^2)/total no of values)
9.	Confidence Intervals = mean +/- (1.96 * (standard_deviation/sqrt(50)))

(1) The driver.py contains the default values from the assumptions made. ie) first entry 0 2 0 - - 
(2) driver.py calls the simulation() funtion under the handsimulation.py file
(3) Simulation values per iteration are returned back to driver.py and printed in output.txt 
(4) The output.txt also has:
	Individual T and D for all 50 batches , followed by, (please scroll to end of file to find the below values)
	1.Mean and Super Mean Time taken for Recertification (T)
	2.Standard Deviation of the mean Time taken for Recertification
	3.Mean and Super Mean Retransmission Time (D)
	4.Standard Deviation of the mean Time taken for Retransmission
	5.Mean of 95th Percentile of the total time for Recertification (T95th)
	6.Standard Deviation of the 95th percentile Time taken for Recertification
	7.Mean of 95th Percentile of the Retransmission time (D95th)
	8.Standard Deviation of the 95th percentile Time taken for Retransmission
	9.Confidence Intervals of Mean of T
	10.Confidence Intervals of Mean of D
	11.Confidence Intervals of Percentile of T
	12.Confidence Intervals of Percentile of D
	
	

