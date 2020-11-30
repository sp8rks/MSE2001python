from mpl_toolkits import mplot3d
#%matplotlib inline
#https://jakevdp.github.io/PythonDataScienceHandbook/04.12-three-dimensional-plotting.html
import numpy as np
import matplotlib.pyplot as plt
fig = plt.figure()
ax = plt.axes(projection='3d')

# def f(x, y):
#     return np.sin(np.sqrt(x ** 2 + y ** 2))

# x = np.linspace(-6, 6, 30)
# y = np.linspace(-6, 6, 30)

# X, Y = np.meshgrid(x, y)
# Z = f(X, Y)


def f(x, y):
    return 1-(x ** 2 + y ** 2)

x = np.linspace(-np.pi, np.pi, 30)
y = np.linspace(-np.pi, np.pi, 30)

X, Y = np.meshgrid(x, y)
Z = f(X, Y)


ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                cmap='viridis', edgecolor='none')
ax.set_title('surface');

# %%
# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

import matplotlib.pyplot as plt
import numpy as np


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create the mesh in polar coordinates and compute corresponding Z.
r = np.linspace(0, 1, 50)
p = np.linspace(0, 2*np.pi, 50)
R, P = np.meshgrid(r, p)
Z = ((R**2 - 1)**2)

# Express the mesh in the cartesian system.
X, Y = R*np.cos(P), R*np.sin(P)

# Plot the surface.
ax.plot_surface(X, Y, Z, cmap=plt.cm.YlGnBu_r)

# Tweak the limits and add latex math labels.
ax.set_zlim(0, 1)
ax.set_xlabel(r'$\phi_\mathrm{real}$')
ax.set_ylabel(r'$\phi_\mathrm{im}$')
ax.set_zlabel(r'$V(\phi)$')

plt.show()

# %%
#https://stackoverflow.com/questions/39408794/python-3d-pyramid
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# vertices of a pyramid
v = np.array([[-1, -1, -1], [1, -1, -1], [1, 1, -1],  [-1, 1, -1], [0, 0, 1]])
ax.scatter3D(v[:, 0], v[:, 1], v[:, 2])

# generate list of sides' polygons of our pyramid
verts = [ [v[0],v[1],v[4]], [v[0],v[3],v[4]],
 [v[2],v[1],v[4]], [v[2],v[3],v[4]], [v[0],v[1],v[2],v[3]]]

# plot sides
#ax.add_collection3d(Poly3DCollection(verts, 
# facecolors='cyan', linewidths=1, edgecolors='r', alpha=.25))

ax.add_collection3d(Poly3DCollection(verts, linewidths=1, edgecolors='r', alpha=.25))


plt.show()
# %%
value=np.arange(0,6,1)
x=[]
y=[]
Z=[]

def f(x, y):
    return 5-x-y

for i in value:
    x.append([i,-i,-i,i])
    y.append([i,i,-i,-i])
    Z.append(-(1-i-1))

X, Y = np.meshgrid(x, y)
Z = f(X,Y)

ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                cmap='viridis', edgecolor='none')
ax.set_title('surface');