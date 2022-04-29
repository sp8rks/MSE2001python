#What about NON-LINEAR equations

#How do we solve this?
#x^2 + y = 5
#x^2 + y^2 = 7

import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(1, figsize=(5,5))

delta = 0.025
x,y = np.meshgrid(np.arange(-4,4.1,delta),np.arange(-4,4.1,delta))

f1 = x**2 + y -5
f2 = x**2 + y**2 -7

plt.contour(x,y,f1,[0])
plt.contour(x,y,f2,[0])
plt.show()

# %%
#using fsolve!
from scipy.optimize import fsolve

def my_function(z):
    x=z[0]
    y=z[1]
    F=np.empty(2)
    F[0]=x**2+y-5
    F[1]=x**2+y**2-7
    return F

# zGuess = np.array([3,3])
# z = fsolve(my_function,zGuess)
# print(z)

array_of_guesses = [np.array([3,-3]),np.array([3,3]),
                    np.array([-3,3]),np.array([-3,-3])]

for guess in array_of_guesses:
    zGuess = guess
    z = fsolve(my_function,zGuess)
    print(z)

# %%
from gekko import GEKKO
m=GEKKO()
x,y = [m.Var(1) for i in range(2)]
m.Equations([x**2+y==5,\
             x**2+y**2==7])
m.solve(disp=False)
print(x.value,y.value)

# %%
import sympy as sym
sym.init_printing()
x,y = sym.symbols('x,y')
f = sym.Eq(x**2+y,5)
g = sym.Eq(x**2+y**2,7)
print(sym.solve([f,g],(x,y)))










