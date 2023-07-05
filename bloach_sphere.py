# Following code is used to visualize the bloch sphere through python for better understanding. 
# used anaconda to run this code. 
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
x = np.outer(np.cos(u), np.sin(v))
y = np.outer(np.sin(u), np.sin(v))
z = np.outer(np.ones(np.size(u)), np.cos(v))
ax.plot_surface(x, y, z, color='b', alpha=0.3)

bloch_vector = np.array([0.5, 0.5, 0.5])
ax.quiver(0, 0, 0, bloch_vector[0], bloch_vector[1], bloch_vector[2], color='r')

ax.text(0, 0, 1.1, "|0⟩", color='black', ha='center')
ax.text(0, 0, -1.1, "|1⟩", color='black', ha='center')

ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])
ax.set_zlim([-1, 1])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

ax.set_box_aspect([1, 1, 1])
ax.set_title('Visualization of Bloch Sphere')


plt.show()


