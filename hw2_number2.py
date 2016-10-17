import matplotlib.pyplot as plt
from scipy import stats

x = [2,4,6,8,10,12,14,16,18,20,22,24]
y = [5.3,14.4,20.7,30.1,35.0,41.3,52.7,55.7,63.0,72.1,80.5,87.9]

sigma = 1.5
slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)

plt.scatter(x,y)
plt.plot([0,26],[intercept,(slope*26 + intercept)])
plt.axis([0,26,0,100])

temp, chi_squared, index = 0, 0, 0

for y_i in y:
	temp = (y_i - (slope * x[index] + intercept)) / sigma
	chi_squared += temp**2
	index += 1

plt.text(2, 90, 'Chi-squared = %s' % chi_squared)
plt.text(2, 80, 'Standard error of\nthe estimate = %s' % std_err)
plt.show()

# The derived formula gave a chi-squared value closer to n = 12 total measurements
# than the Scipy package, though both appeared to be good linear fits visually.