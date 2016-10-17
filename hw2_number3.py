import matplotlib.pyplot as plt
from scipy import stats
import math

x = [2,4,6,8,10,12,14,16,18,20,22,24]
y = [5.3,14.4,20.7,30.1,35.0,41.3,52.7,55.7,63.0,72.1,80.5,87.9]

sigma = 1.5
slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
sumxy, sumx2, index = 0, 0, 0

for x_i in x:
	sumx2 += x_i**2
	sumxy += x_i * y[index]
	index += 1
	
b = sumxy / sumx2

plt.scatter(x,y,color = 'b')
plt.errorbar(x,y,yerr = sigma,fmt = 'none',ecolor = 'b')
plt.plot([0,26],[0,(b*26)],color = 'r')
plt.plot([0,26],[intercept,(slope*26 + intercept)],color = 'g')
plt.axis([0,26,0,100])

temp1, chi_squared1, temp2, chi_squared2, index = 0, 0, 0, 0, 0

for y_i in y:
	temp1 = (y_i - (b * x[index])) / sigma
	chi_squared1 += temp1**2
	temp2 = (y_i - (slope * x[index] + intercept)) / sigma
	chi_squared2 += temp2**2
	index += 1

sigma_b = sigma / math.sqrt(sumx2)

plt.text(2, 85, 'Chi-squared of\ncalculated fit = %s' % chi_squared1, color = 'r')
plt.text(2, 80, 'Uncertainty in b = %s' % sigma_b, color = 'r')
plt.text(12, 20, 'Chi-squared of\nPython fit = %s' % chi_squared2, color = 'g')
plt.text(12, 10, 'Standard error of\nthe estimate = %s' % std_err, color = 'g')
plt.show()