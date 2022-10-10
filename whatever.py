import matplotlib.pyplot as plt
import numpy as np

point_cloud_data = []
i = 0
noise = 0.2

while i < 200:
    X = i/50
    Y = np.cos(i) + noise * (np.random.rand(1)[0] - 0.5)
    Z = np.sin(i) + noise * (np.random.rand(1)[0] - 0.5)
    coord = [X, Y, Z]
    point_cloud_data.append(coord)
    i +=1

xdata = [coordinate[0] for coordinate in point_cloud_data]
ydata = [coordinate[1] for coordinate in point_cloud_data]
zdata = [coordinate[2] for coordinate in point_cloud_data]

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.scatter(xdata, ydata, zdata, c=zdata)
plt.show()