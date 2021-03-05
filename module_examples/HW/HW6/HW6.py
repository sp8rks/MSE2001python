# IMPORTS (YOU CAN ADD MORE IF NEEDED)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import fsolve, minimize, curve_fit
from scipy.integrate import odeint
import pint
import scipy.constants as cnst
from molmass import Formula

# ASSIGNMENT 6 (Week 6, Solving Equations)
# =============================================================================
# I have defined a student "class". This outlines what a student object is.
# ******************************************************************
# ************FILL THIS OUT WITH YOUR INFO!!!!!!!*******************
# ******************************************************************
class Student():
    def __init__(self, first_name, last_name, u_id, email):
        self.assignment = 6
        self.description = "HW6, Solving Equations"
        self.due_date = "Mar 5, 2021"
        self.first_name = first_name #put your first name here
        self.last_name = last_name #put your last name here
        self.u_id = u_id #put your unid here
        self.email = email #put your utah.edu email here
        self.HWScores = {} 

    def get_final_score(self):
        self.final_score = 0
        for score in self.HWScores.values():
            self.final_score += score
        return self.final_score


# FILL THIS OUT SECTION SO IT IS EASY FOR ME TO AUTO GRADE THINGS.
student = Student(first_name='first', last_name='last',
                  u_id='uXXXXXXX', email='email@email.com')
# set global fontsize to 20
plt.rcParams.update({'font.size': 14})


# %%
# =============================================================================
#     Q(example 0)
#        Solve for the constants that satisfy the given equations.
#        (using numpy's linear algebra solver)
#        Equation 1: 3 * w0 + 12 * w1 - 13 * w2 = 8
#        Equation 2: 13 * w0 - w2 = 13
#        Equation 3: w0 + w1 + w2 = 0
# =============================================================================
def example_0():
    coefficients = np.array([[3, 12, -13], [13, 0, -1], [1, 1, 1]])
    constants = np.array([8, 13, 0])
    w_values = np.linalg.solve(coefficients, constants)
    return w_values


# ###### CODE BLOCK TO DETERMINE WHETHER THE FUNCTION WORKS AS INTENDED ##### #
Qe0_my_ans = example_0()
Qe0_ans = [0.9491018, -0.28742515, -0.66167665]

# ###### CODE BLOCK TO DETERMINE WHETHER THE FUNCTION WORKS AS INTENDED ##### #

# %%
# =============================================================================
#     Q(example 1) SOLVE A SIMPLE ODE
#        the ODE, dy/dx + y = x, y(0) = 1 can be analytically solved to get
#        the equation y(x) = x + 2*exp(-x) - 1.
# =============================================================================
# Define a function which calculates the derivative
def dy_dx(y, x):
    return x - y


xs = np.linspace(0, 10, 25)
y0 = 1.0  # the initial condition
ys = odeint(dy_dx, y0, xs)
ys = np.array(ys).flatten()

y_exact = xs - 1 + 2*np.exp(-xs)
plt.figure(figsize=(5, 5))
plt.plot(xs, ys, label='numeric solution')
plt.plot(xs, y_exact, "o", label='analytic solution')
plt.xlabel('x-values')
plt.ylabel('y-values')
plt.legend()


# %%
# =============================================================================
#     Q(example 2) Ficks first law is: J = -D * d(phi)/d(x)
#        https://en.wikipedia.org/wiki/Fick%27s_laws_of_diffusion
#        write a function for Ficks law. Use odeint and Ficks first law to
#        generate diffussion solutions numerically. 
# =============================================================================
def ficks_first_law(phi, x, d_const, j):
    dphi_dx = j / (-d_const)
    return dphi_dx

j = 1
d_const = 1
phi0 = 10
range_x = (0, 10)
xs = np.linspace(*range_x, 200)
numeric_phi = odeint(ficks_first_law, phi0, xs, args=(j, d_const))

plt.figure(figsize=(5, 5))
plt.plot(numeric_phi, xs, label='numerical Ficks 1st')

phi_final = j / -(d_const) * range_x[1] - range_x[0] + phi0
plt.plot([phi_final, phi0], [range_x[1], range_x[0]],
         'o', label='data points')
plt.legend()
plt.xlabel('thickness (units)')
plt.ylabel('concentration (units)')

# %%
# =============================================================================
#     Q0 Solve for the constants that satisfy the given equations.
#        (using numpy's linear algebra solver)
#        Equation 1: 14.7 * w0 - 0.01 * w1 - 13 * w2 -13 = 8
#        Equation 2: 13 * w0 - w2 -5 * w3 = 13
#        Equation 3: 14 * w0 + -2 * w1 + w2 = 0
#        Equation 4: w0 + w1 + 2 * w2 -4.16 = 0
#        put your code in a function called q0 that has no inputs but returns
#        an array of floats
# =============================================================================
#function q0










# ###### CODE BLOCK TO DETERMINE WHETHER THE FUNCTION WORKS AS INTENDED ##### #
Q0_my_ans = q0()
Q0_ans = [0.75810404,  4.92576183, -0.76193294, -0.4765429]
correct = np.allclose(Q0_my_ans, Q0_ans)
if correct:
    print('Q0 is correct')
    student.HWScores['Q0'] = 1  # add score for correct execution
else:
    print('Check your code for Q0')
# ###### CODE BLOCK TO DETERMINE WHETHER THE FUNCTION WORKS AS INTENDED ##### #


# %%
# =============================================================================
#     Q1 To get you ready for the final project, let's do some stoichiometry 
#     calculations using python!
#     For the unbalanced equation below, figure out how many grams of NaOH
#     are needed to consume 5 grams of H2SO4. You must use pint and molmass 
#     formula libraries for this problem. Save your answer in the pint object
#     mass_NaOH with mass in grams
#     NaOH + H2SO4 -> H2O + Na2SO4
#     BALANCE THIS EQUATION FIRST. IF YOU HAVEN'T TAKEN GEN CHEM YET, COME TALK
#     TO PROF SPARKS OR THE TA'S AND WE WILL DO THIS TOGETHER
# =============================================================================









# ###### CODE BLOCK TO DETERMINE WHETHER THE FUNCTION WORKS AS INTENDED ##### #
Q1_my_ans = mass_NaOH.magnitude
Q1_ans = 4.078
correct = np.isclose(Q1_my_ans, Q1_ans,atol=0.01)
if correct:
    print('Q1 is correct')
    student.HWScores['Q1'] = 1  # add score for correct execution
else:
    print('Check your code for Q1')
# ###### CODE BLOCK TO DETERMINE WHETHER THE FUNCTION WORKS AS INTENDED ##### #


# %%
# =============================================================================
#     Q2 Solve for the roots of this equation.
#        (use fsolve)
#        Equation: 3 * x**2 + 14 * x = 10
#     as you can see in the check code block, this question requires you to 
#     create a function q2 which takes nothing as an input, but returns a float
# =============================================================================










# ###### CODE BLOCK TO DETERMINE WHETHER THE FUNCTION WORKS AS INTENDED ##### #
Q2_my_ans = q2()
Q2_ans = [0.62939814]
correct = np.allclose(Q2_my_ans, Q2_ans)
if correct:
    print('Q2 is correct')
    student.HWScores['Q2'] = 1  # add score for correct execution
else:
    print('Check your code for Q2')
# ###### CODE BLOCK TO DETERMINE WHETHER THE FUNCTION WORKS AS INTENDED ##### #


# %%
# =============================================================================
#     Q3 Solve for the value of x that determines the intersection of two
#        nonlinear equations.
#        Equation 1: x**2 = 0
#        Equation 2: exp(x) + 3 = 0
#        Plot the equations and any roots you find. Make your plots look good!
# =============================================================================









# ###### CODE BLOCK TO DETERMINE WHETHER THE FUNCTION WORKS AS INTENDED ##### #
correct = False  # change to True if your plot verifies your solution.
if correct:
    print('Q3 is correct')
    student.HWScores['Q3'] = 1  # add score for correct execution
else:
    print('Check your code for Q3')
# ###### CODE BLOCK TO DETERMINE WHETHER THE FUNCTION WORKS AS INTENDED ##### #



# %%
# =============================================================================
#     Q4 Read the data in from the hall_petch.csv file. Your task is to fit 
#     this data to the Hall-Petch equation which has the form 
#     y=sigma+k*x^(-0.5)
#     use any method you like. When done, save the parameters for sigma and k
#     in variables sigma and k.
# =============================================================================











# ###### CODE BLOCK TO DETERMINE WHETHER THE FUNCTION WORKS AS INTENDED ##### #
# sigma = YOUR SIGMA HERE
# k = YOUR K HERE
Q4_my_ans = [sigma,k]
Q4_ans = [1.10146,1.73451]
correct = np.allclose(Q4_my_ans, Q4_ans)
if correct:
    print('Q4 is correct')
    student.HWScores['Q4'] = 1  # add score for correct execution
else:
    print('Check your code for Q4')
# ###### CODE BLOCK TO DETERMINE WHETHER THE FUNCTION WORKS AS INTENDED ##### #


# %%
# =============================================================================
#     Q5 This HW is hard enough. Let's skip this one ;)
# =============================================================================

student.HWScores['Q5'] = 1  # add freebie point for this question


# %%
# =============================================================================
#     Q6 You have been asked to look at heat capacity data that was collected
#        by the new employee Dennis Nedry. You are not sure if you can trust 
#        his data.
#        You can be resonable sure that if the data looks well behaved it was
#        probably done correctly.
#
#        Read in the heat capacity data and visualize it by plotting the heat
#        capacity versus temperature for each sample.
#        Make your plots look good! (label axis, nice ticks, good markers, etc)
# =============================================================================










# %%
# =============================================================================
#     Q7 The data seems to be very well-recorded. Your lab expects to use these
#        values often.
#        You have been asked to fit heat capacity data to the expansion:
#        Cp = a + b * T + c * T**2 + d * T**3
#
#        Please create a function that will, given a materials formula, will
#        return [a, b ,c, d]
#
#        Check your results using the material "Al2Be1O4".
#        Plot your fit over the real data to ensure you are correct.
# =============================================================================












# ###### CODE BLOCK TO DETERMINE WHETHER THE FUNCTION WORKS AS INTENDED ##### #
formula = "Al2Be1O4"
coeffs = get_coefficients(formula)
coeffs_ans = [3.4914e+01,  3.1001e-01, -2.2563e-04,  5.7143e-08]
correct = np.allclose(coeffs, coeffs_ans, atol=1e-5)
if correct:
    print('Q7 is correct')
    student.HWScores['Q7'] = 1  # add score for correct execution
else:
    print('Check your code for Q7')
# ###### CODE BLOCK TO DETERMINE WHETHER THE FUNCTION WORKS AS INTENDED ##### #


# %%
# =============================================================================
#     Q8 Get the coefficients for all materials formulas in the given csv file.
#        Ensure that your fits are reasonable. They should be good, but don't
#        have to be perfect.
# =============================================================================









# %%
# =============================================================================
#     Q9 Save, in a csv, the chemical formula, and the four coefficients.
# =============================================================================








