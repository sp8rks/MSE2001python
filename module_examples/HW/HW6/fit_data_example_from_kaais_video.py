import numpy as np
import matplotlib.pyplot as plt
import scipy.special as sc
from scipy.optimize import minimize
from scipy.optimize import fsolve
import pandas as pd

# %%
# example data
np.random.seed(1)
x_data = np.array(np.arange(0, 200, 5))
y_data_ideal = 15*x_data-2*x_data**1.5+7*np.exp(x_data**0.34)
y_data = (15*x_data-2*x_data**1.5+7*np.exp(x_data**0.34))+np.random.normal(0, 15, len(x_data))

plt.figure(1, figsize=(7,7))
font = {'family': 'DejaVu Sans',
        'weight': 'normal',
        'size': 20}
plt.rc('font', **font)
plt.tick_params(direction='in', length=10, bottom=True, top=True, left=True, right=True)

# plot the real underlying trend
plt.plot(x_data, y_data, 'r*', label='example data')
plt.plot(x_data, y_data_ideal, 'b-', label='ideal')
# plot the 'measured' trend after applying a normal distribution to the data
plt.legend()
plt.show()

# %%

# LOAD YOUR DATA HERE
# x_data = np.array([1, 2, 3, 4, 5])
# y_data = np.array([10, 20, 30, 40, 50])


# calculate y
def calculate_y_fit(parameters, x_data):
    '''
    Parameters
    ----------
    parameters: np.array()
        A single vector containing the optimization parameters, ``parameters`` (1-D array of points)

    Return
    ----------
    y:array
        function value y = f(X)
        
    Example
    -------
    Optimization of function f(a, b, c) to fit experimental data:
    
    >>> def example_function(parameters, x_data):
    >>>     ### WRITE YOUR FUNCTION HERE ###
    >>>     a = parameters[0]
    >>>     b = parameters[1]
    >>>     c = parameters[2]
    >>>     y = a*x_data+b^2*x_data+c*x_data
    >>>     return y
    '''
    ### DELETE EXAMPLE AND WRITE YOUR FUNCTION HERE ###
    a = parameters[0]
    b = parameters[1]
    c = parameters[2]
    d = parameters[3]
    y = a*x_data-b*x_data**1.5+c*np.exp(x_data**d)
    return y


# define the objective
def objective(parameters, x_data, y_data):
    '''
    Here we want define the objective function which we will seek to miminize.
    Here the objective sums the squared error. If this is minimized, we have a
    good fit.

    Parameters
    ----------
    parameters: np.array()
        A single vector containing the optimization parameters, ``parameters`` (1-D array of points)
    x_data: np.array()
        A single vector containing the experimental x_data
    y_data: np.array()
        A single vector containing the experimental y_data
    '''
    # calculate y
    y_fit = calculate_y_fit(parameters, x_data)
    # calculate objective
    obj = 0.0
    for i in range(len(y_data)):
        obj += np.sqrt((y_fit[i]-y_data[i])**2)
    # return result
    return obj

# initial guesses (this might have to be played with to get complex equations
# to fit. Often times the solver can get stuck or explode if the guess is bad)
x0 = np.zeros(4)  # CREATE AN ARRAY OF SIZE N, WHERE N=Number of Parameters
x0[0] = 55 # actual, a=15
x0[1] = 22 # actual, b=2
x0[2] = 21 # actual, c=7
x0[3] = 0.6 # actual, d=0.34

# show initial objective
print('Initial SSE Objective: ' + str(objective(x0, x_data, y_data)))

# optimization step (minimize the objective)
# set bounds on variables if necessary
#pos_bnds = (-1.0e10, 1.0e10)
#bnds = (pos_bnds, pos_bnds)
solution = minimize(fun=objective, x0=x0, args=(x_data, y_data), method='Nelder-Mead')
x = solution.x
y = calculate_y_fit(x, x_data)

#y = calc_y([1e-12, 11000])
# show final objective
print('Final SSE Objective: ' + str(objective(x0, x_data, y)))

# %%
plt.figure(1, figsize=(6, 6))
font = {'family': 'DejaVu Sans',
        'weight': 'normal',
        'size': 18}
plt.rc('font', **font)
plt.tick_params(direction='in', length=10, bottom=True, top=True, left=True, right=True)
plt.plot(x_data, y_data, 'r*', label='example data')
plt.plot(x_data, y, 'k--', label='best fit')
plt.xlabel('ex$\\alpha$mple x-axis $using\\;LaTex\\;(\\alpha)\\;(\\beta)\\;$ ($\\frac{m^2}{s}$)')
plt.ylabel('example y-axis (units)')
plt.ylim(0, 400)
plt.legend()
#plt.savefig('results.png')  # this will save your figure to the current directory
plt.show()