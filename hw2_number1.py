import matplotlib.pyplot as plt
import math

x = [2,4,6,8,10,12,14,16,18,20,22,24]
y = [5.3,14.4,20.7,30.1,35.0,41.3,52.7,55.7,63.0,72.1,80.5,87.9]

sumxy, sumx2, index = 0, 0, 0
sigma = 1.5

for x_i in x:
	sumx2 += x_i**2
	sumxy += x_i * y[index]
	index += 1
	
b = sumxy / sumx2

plt.scatter(x,y)
plt.plot([0,26],[0,(b*26)])
plt.axis([0,26,0,100])

temp, chi_squared, index = 0, 0, 0

for y_i in y:
	temp = (y_i - (b * x[index])) / sigma
	chi_squared += temp**2
	index += 1

sigma_b = sigma / math.sqrt(sumx2)

plt.text(2, 90, 'Chi-squared = %s' % chi_squared)
plt.text(2, 80, 'Uncertainty in b = %s' % sigma_b)
plt.show()