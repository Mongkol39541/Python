import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.quiver(0, 0, 0, -2, -2, 36)
ax.quiver(0, 0, 0, 2, 0, -2)
ax.quiver(0, 0, 0, -5, 1, 0)
ax.set_xlim([-12, 4])
ax.set_ylim([-12, 4])
ax.set_zlim([-12, 4])
plt.show()