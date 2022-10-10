import numpy as np 
import matplotlib.pyplot as plt 
from scipy.stats import norm, t

x = np.arange(-5, 5, 0.001)

y1 = norm.pdf(x, -1, 1.5)
y2 = norm.pdf(x, 1, 1.5)
y11 = norm.pdf(x, -1, 1.5)
y22 = norm.pdf(x, 1, 1.5)


plt.plot(x, y1, c='r', alpha=0)
plt.plot(x, y2, c='g', alpha=0)
plt.plot(x, y11, alpha=0)
plt.plot(x, y22, alpha=0)

plt.ylabel('Probability')
plt.xlabel('Internal Strength')
plt.xticks([])
plt.yticks([])
plt.fill_between(x, y1, color='r', where=x<0, alpha=1)
plt.fill_between(x, y2, color='g', where=x>0, alpha=1)
plt.fill_between(x, y11, color='maroon', where=x>0, alpha=1)
plt.fill_between(x, y22, color='darksalmon', where=x<0, alpha=1)
plt.axvline(x = 0, ymin=0.05, ymax=0.77, color = 'black')
plt.show()