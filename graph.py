import numpy as np
import matplotlib.pyplot as plt

def gauss(x, mu, sigma):

	return 1/(sigma*np.sqrt(2*np.pi))*np.exp(-(x - mu)**2/(2*sigma**2))

with open("Fe_H.txt") as f:
	numbers1 = []
	for line in f:
		numbers1.append(float(line))
f.close()

n1 = np.arange(-0.9,-0.2,0.001)

plt.figure(1)
plt.subplot(511)
plt.plot(n1, gauss(n1, -0.54191489, 0.11322617),color='r')
plt.hist(numbers1, 60, facecolor='r')
plt.xlabel('Fe_H')
plt.ylabel('Number of Occurrences')
plt.title('Metallicity Index of Arcturus')
plt.text(-0.8, 5, r'$\mu=-0.54191489,\ \sigma=0.11322617$')
plt.axis([-0.9, -0.2, 0, 7])
plt.grid(True)

with open("oRV.txt") as f:
	numbers2 = []
	for line in f:
		numbers2.append(float(line))
f.close()

n2 = np.arange(-9,-2,0.01)

plt.subplot(512)
plt.plot(n2, gauss(n2, -5.41842105, 1.12534806),color='r')
plt.hist(numbers2, 60, facecolor='b')
plt.xlabel('oRV (km/s)')
plt.ylabel('Number of Occurrences')
plt.title('Radial Velocity of Arcturus')
plt.text(-8, 3, r'$\mu=-5.41842105,\ \sigma=1.12534806$')
plt.axis([-9, -2, 0, 4])
plt.grid(True)
		
with open("PLX.txt") as f:
	numbers3 = []
	for line in f:
		numbers3.append(float(line))
f.close()

n3 = np.arange(0.075,0.1,0.0001)

plt.subplot(513)
plt.plot(n3, gauss(n3, 0.08812499, 0.00559177),color='r')
plt.hist(numbers3, 7, facecolor='y')
plt.xlabel('PLX (arsec)')
plt.ylabel('Number of Occurrences')
plt.title('Parallax of Arcturus')
plt.text(0.0785, 60, r'$\mu=0.08812499,\ \sigma=0.00559177$')
plt.axis([0.075, 0.1, 0, 80])
plt.grid(True)

with open("PM.txt") as f:
	numbers4 = []
	for line in f:
		numbers4.append(float(line))
f.close()

n4 = np.arange(-1115,-1080,0.01)

plt.subplot(514)
plt.plot(n4, gauss(n4, -1097.0, 8.34266144),color='r')
plt.hist(numbers4, 5, facecolor='g')
plt.xlabel('PM (mas/yr)')
plt.ylabel('Number of Occurrences')
plt.title('Proper Motion R.A. of Arcturus')
plt.text(-1110, 1.5, r'$\mu=-1097.0,\ \sigma=8.34266144$')
plt.axis([-1115, -1080, 0, 2])
plt.grid(True)
		
with open("Velocities.txt") as f:
	numbers5 = []
	for line in f:
		numbers5.append(float(line))
f.close()

n5 = np.arange(-9,-2,0.01)

plt.subplot(515)
plt.plot(n5, gauss(n5, -5.37279069, 1.06723792),color='r')
plt.hist(numbers5, 40, facecolor='m')
plt.xlabel('Velocities (km/s)')
plt.ylabel('Number of Occurrences')
plt.title('Velocity of Arcturus')
plt.text(-8, 5, r'$\mu=-5.37279069,\ \sigma=1.06723792$')
plt.axis([-9, -2, 0, 7])
plt.grid(True)

plt.show()