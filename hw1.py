import math
import statistics

def main():

	Fe_H_mean = calcMean("Fe_H.txt")
	Fe_H_median = calcMedian("Fe_H.txt")
	Fe_H_mode = calcMode("Fe_H.txt")
	Fe_H_stddev = calcStdDev("Fe_H.txt")
	
	print ("Fe_H:\n\tMean: %s\n\tMedian: %s" % (Fe_H_mean,Fe_H_median))
	print ("\tMode: %s\n\tStandard Deviation: %s" % (Fe_H_mode,Fe_H_stddev))
	
	oRV_mean = calcMean("oRV.txt")
	oRV_median = calcMedian("oRV.txt")
	oRV_mode = calcMode("oRV.txt")
	oRV_stddev = calcStdDev("oRV.txt")
	
	print ("\noRV:\n\tMean: %s\n\tMedian: %s" % (oRV_mean,oRV_median))
	print ("\tMode: %s\n\tStandard Deviation: %s" % (oRV_mode,oRV_stddev))
	
	PLX_mean = calcMean("PLX.txt")
	PLX_median = calcMedian("PLX.txt")
	PLX_mode = calcMode("PLX.txt")
	PLX_stddev = calcStdDev("PLX.txt")
	
	print ("\nPLX:\n\tMean: %s\n\tMedian: %s" % (PLX_mean,PLX_median))
	print ("\tMode: %s\n\tStandard Deviation: %s" % (PLX_mode,PLX_stddev))
	
	PM_mean = calcMean("PM.txt")
	PM_median = calcMedian("PM.txt")
	PM_mode = calcMode("PM.txt")
	PM_stddev = calcStdDev("PM.txt")
	
	print ("\nPM:\n\tMean: %s\n\tMedian: %s" % (PM_mean,PM_median))
	print ("\tMode: %s\n\tStandard Deviation: %s" % (PM_mode,PM_stddev))
	
	Velocities_mean = calcMean("Velocities.txt")
	Velocities_median = calcMedian("Velocities.txt")
	Velocities_mode = calcMode("Velocities.txt")
	Velocities_stddev = calcStdDev("Velocities.txt")

	print ("\nVelocities:\n\tMean: %s\n\tMedian: %s" % (Velocities_mean,Velocities_median))
	print ("\tMode: %s\n\tStandard Deviation: %s" % (Velocities_mode,Velocities_stddev))
	
def calcMean(filename):

	with open(filename) as f:
		numbers = []
		for line in f:
			numbers.append(float(line))
		
	mean = sum(numbers) / len(numbers)
	
	f.close()
	
	return mean

def calcMedian(filename):

	with open(filename) as f:
		numbers = []
		for line in f:
			numbers.append(float(line))
		numbers.sort()
	
	median = statistics.median(map(float, numbers))
	
	f.close()
	
	return median

def calcMode(filename):

	with open(filename) as f:
		numbers = []
		for line in f:
			numbers.append(float(line))
		numbers.sort()
			
	mode = statistics.mode(map(float, numbers))
	
	f.close()
	
	return mode
	
def calcStdDev(filename):

	with open(filename) as f:
		numbers = []
		for line in f:
			numbers.append(float(line))
	
	stddev = statistics.stdev(map(float, numbers))
	
	f.close()
	
	return stddev
	
main()
