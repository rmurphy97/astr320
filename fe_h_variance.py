import statistics

def main():

	Fe_H_sVar = SampleVar("Fe_H.txt")
	Fe_H_pVar = ParentVar("Fe_H.txt")
	
	print ("Fe_H Sample Variance: ",Fe_H_sVar)
	print ("Fe_H Parent Variance: ",Fe_H_pVar)
	
	print ("Python reports both variances in its native functions.")

def SampleVar(filename):

	with open(filename) as f:
		numbers = []
		for line in f:
			numbers.append(float(line))
	
	sVar = statistics.variance(map(float, numbers))
	
	f.close()
	
	return sVar

def ParentVar(filename):

	with open(filename) as f:
		numbers = []
		for line in f:
			numbers.append(float(line))
	
	pVar = statistics.pvariance(map(float, numbers))
	
	f.close()
	
	return pVar	
	
main()