# IMPORTS
import numpy as np
import matplotlib.pyplot as plt

# ASSIGNMENT 2 (Week 2, Functions, conditions, classes)
# =============================================================================
# NOTE: The """docstring""" (the text that lets you know how to use a
#       function) uses the word "Parameters". The "Parameters" in the
#       docstring's text refers to the "arguments" of your function.

# =============================================================================
#     Q(example 0)
#        Write a function that returns the energy of light given its frequency.
# =============================================================================
# function name: energy_of_light
def energy_of_light(v):
    """
    The energy of light can be described by the equation: E = hv

    Parameters
    ----------
    v : float
        The frequency of light (s-1).

    Returns
    -------
    E : float
        The energy (J)
    """
    h = 6.62607004e-34  # J s
    E = h * v  # compute energy of light given input "v"
    return E


# ###### CODE BLOCK TO DETERMINE WHETHER THE FUNCTION WORKS AS INTENDED ##### #
v = 1e18  # s-1
your_answer = energy_of_light(v)
print('You answered {}'.format(your_answer))
answer = 6.6260e-16

# check that the answer is close to the correct answer
if np.isclose(your_answer, answer):
    print('example 0: You are correct')
else:
    print('Check your code')
# ###### CODE BLOCK TO DETERMINE WHETHER THE FUNCTION WORKS AS INTENDED ##### #


# %%
# =============================================================================
#     Q(example 1)
#        Write a function that can calculate the temperature-dependent
#        diffusion coefficient.
#
#        This function should have the following arguments:
#            - D0, The temperature-independent diffusion constant.
#            - Qd, The activation energy for diffusion.
#            - temp, The temperature of interest
#
#        This function should output the temperature-dependent diffusion
#        coefficient defined by the relation:
#        Dt = D0 * np.exp(-Qd / r_ideal / temp)
# =============================================================================
# function name: diffusion
def diffusion(D0, Qd, temp):
    """
    Calculate the temperature dependent diffusion coefficient.

    Parameters
    ----------
    D0 : float
        Temperature-independdent constant.
    Qd : float
        Activation energy for diffusion.
    temp : float
        Temperature.

    Returns
    -------
    diffusion_coeff : float
        Temperature dependent diffusion coefficient.

    """
    r_ideal = 8.314  # (J mol-1 k-1)
    diffusion_coeff = D0 * np.exp(-Qd / r_ideal / temp)
    return diffusion_coeff


# ###### CODE BLOCK TO DETERMINE WHETHER THE FUNCTION WORKS AS INTENDED ##### #
D0 = 1.2e-4  # m^2 s-1
Qd = 131  # kJ mol-1
temp = 550  # C

# correct the units
Qd = Qd * 1000  # j mol-1
temp = temp + 273.15

# if you function is correct, it will generate the correct value here
your_answer = diffusion(D0, Qd, temp)
print('example 1: You answered {}'.format(your_answer))
answer = 5.835e-13

# check that the answer is close to the correct answer
if np.isclose(your_answer, answer):
    print('You are correct')
else:
    print('Check your code')
# ###### CODE BLOCK TO DETERMINE WHETHER THE FUNCTION WORKS AS INTENDED ##### #

# ###### visualize our results
temps = list(range(200, 1700))
diffusion_coeff = [diffusion(D0, Qd, temp) for temp in temps]
plt.plot(temps, diffusion_coeff, 'rx')
plt.show()


# %%
# =============================================================================
#     Q0 Make a function that converts Fahrenheit to Celsius.
#        The equation for this:  C = (F - 32) * 5 / 9
# =============================================================================
# create a function to convert away from the barbaric "Imperial" units
# function name: fahrenheit_to_celsius













# ###### CODE BLOCK TO DETERMINE WHETHER THE FUNCTION WORKS AS INTENDED ##### #
temp_F = 42.8
your_answer = fahrenheit_to_celsius(temp_F)
print('Q0: You answered {}'.format(your_answer))
answer = 6

if np.isclose(your_answer, answer):
    print('You are correct')
    student.HWScores[0] = 1  # add score for correct execution of Q0
else:
    print('Check your code')
# ###### CODE BLOCK TO DETERMINE WHETHER THE FUNCTION WORKS AS INTENDED ##### #


# %%
# =============================================================================
#     Q1 Make a function to calculate the hypotenuse of a right triangle
#        when given the two short sides as the function arguments.
# =============================================================================
# function to compute the hypotenuse
# function name: pythagorean_theorem













# ###### CODE BLOCK TO DETERMINE WHETHER THE FUNCTION WORKS AS INTENDED ##### #
a = 3
b = 4
your_answer = pythagorean_theorem(a, b)
print('Q1: You answered {}'.format(your_answer))
answer = 5

if np.isclose(your_answer, answer):
    print('You are correct')
else:
    print('Check your code')
# ###### CODE BLOCK TO DETERMINE WHETHER THE FUNCTION WORKS AS INTENDED ##### #


# %%
# =============================================================================
#     Q2 Create the quadratic formula.
#        Your equation should return a list.
#        In that list you should have the two roots of "x".
#        The function arguments should be the coefficients a, b, and c
#        corresponding to the equation: 0 = a * x**2 + b * x + c
# =============================================================================
# Function to get roots for second degree polynomial
# function name: quadratic_formula












# ###### CODE BLOCK TO DETERMINE WHETHER THE FUNCTION WORKS AS INTENDED ##### #
# solve the polynomial 1x^2 - 4x + 2 = 0
a = 1
b = 3
c = -4
your_answer = quadratic_formula(a, b, c)
print('Q2: You answered {}'.format(your_answer))
answer = [1, -4]

if all(np.isclose(your_answer, answer)):
    print('You are correct')
else:
    print('Check your code')
# ###### CODE BLOCK TO DETERMINE WHETHER THE FUNCTION WORKS AS INTENDED ##### #


# %%
# =============================================================================
#     Q3 Build an equation that extracts the run parameters from the given
#        list of file names (stored as strings).

#        - Each "run" is represented by a string.
#        - Your equation should take individual strings as an input.
#        - Your equation should return a value for alpha and a value for the
#        temperature.
#        - These values should be returned as floats.
# =============================================================================
file_names = ['alpha_1.1mm_temp_220K.csv',
              'alpha_1.3mm_temp_230K.csv',
              'alpha_1.5mm_temp_240K.csv',
              'alpha_1.3mm_temp_250K.csv',
              'alpha_1.7mm_temp_260K.csv',
              'alpha_1.7mm_temp_270K.csv',
              'alpha_1.8mm_temp_280K.csv',
              'alpha_1.9mm_temp_290K.csv',
              'alpha_1.11mm_temp_300K.csv',
              'alpha_1.12mm_temp_310K.csv',
              'alpha_1.11mm_temp_320K.csv',
              'alpha_1.13mm_temp_330K.csv',
              'alpha_1.14mm_temp_340K.csv',
              'alpha_1.16mm_temp_350K.csv',
              'alpha_1.17mm_temp_360K.csv',
              'alpha_1.19mm_temp_370K.csv']

# parse the string to get desired values as "float" type's
# function name: parse_string













# ###### CODE BLOCK TO DETERMINE WHETHER THE FUNCTION WORKS AS INTENDED ##### #
# these are like "for loops" this technique is called list comprehension
your_answers = [parse_string(file) for file in file_names]
your_alphas = [val[0] for val in your_answers]
your_temps = [val[1] for val in your_answers]

alphas = [1.1, 1.3, 1.5, 1.3, 1.7, 1.7, 1.8, 1.9, 1.11, 1.12, 1.11, 1.13, 1.14,
          1.16, 1.17, 1.19]
temps = [220.0, 230.0, 240.0, 250.0, 260.0, 270.0, 280.0, 290.0, 300.0, 310.0,
         320.0, 330.0, 340.0, 350.0, 360.0, 370.0]

if all(np.isclose(your_alphas, alphas)):
    print("Q3: Your alpha's are correct")
else:
    print("Incorrect alpha's. Check your code")

if all(np.isclose(your_temps, temps)):
    print("Q3: Your temps's are correct")
else:
    print("Incorrect temps's. Check your code")
# ###### CODE BLOCK TO DETERMINE WHETHER THE FUNCTION WORKS AS INTENDED ##### #


# %%
# =============================================================================
#     Q4 Build a function that accepts a dictionary containing lattice 
#       parameters a, b, and c as well as angles alpha, beta, and gamma all 
#       stored as keywords with values and then returns the crystal system. 
#       (cubic, orthorhombic, tetragonal, hexagonal, trigonal, monoclinic, or 
#       triclinic)
# =============================================================================

# function name: crystal_system_classifier













# ###### CODE BLOCK TO DETERMINE WHETHER THE FUNCTION WORKS AS INTENDED ##### #
compound = {'a':5.245,'b':5.245,'c':7.000,'alpha':90,'beta':90,'gamma':120}
your_answer = crystal_system_classifier(compound)
print('Q4: You answered {}'.format(your_answer))
answer = 'hexagonal'
if answer == your_answer:
    print("You are correct")
else:
    print("Incorrect crystal system. Check your code")
###### CODE BLOCK TO DETERMINE WHETHER THE FUNCTION WORKS AS INTENDED ##### #


# %%
# =============================================================================
#     Q5 Build a function that accepts the price of a meal and a rating (1-5)
#       and then returns an appropriate tip amount.
# =============================================================================
# function goes here
# function name: appropriate_tip













# ###### CODE BLOCK TO DETERMINE WHETHER THE FUNCTION WORKS AS INTENDED ##### #
try:
    your_answer = appropriate_tip(your_inputs)  # will inspect this one.
except:
    print("there seems to be an issue with your function")
# ###### CODE BLOCK TO DETERMINE WHETHER THE FUNCTION WORKS AS INTENDED ##### #



# %%
# =============================================================================
#     Q6 Build function that operates as an "and" gate
# =============================================================================
# function goes here
# function name: and_gate











# ###### CODE BLOCK TO DETERMINE WHETHER THE FUNCTION WORKS AS INTENDED ##### #
ans1 = [and_gate(1, 1) == 1,
       and_gate(1, 0) == 0,
       and_gate(0, 1) == 0,
       and_gate(0, 0) == 0]
print('Q4: You answered {}'.format(ans))

if all(ans1):
    print("You are correct")
else:
    print("Incorrect logic. Check your code")
# ###### CODE BLOCK TO DETERMINE WHETHER THE FUNCTION WORKS AS INTENDED ##### #


# %%
# =============================================================================
#     Q7 Build function that operates as an "or" gate
# =============================================================================
# function goes here
# function name: or_gate












# ###### CODE BLOCK TO DETERMINE WHETHER THE FUNCTION WORKS AS INTENDED ##### #
ans2 = [or_gate(1, 1) == 0,
       or_gate(1, 0) == 1,
       or_gate(0, 1) == 1,
       or_gate(0, 0) == 1]
print('Q4: You answered {}'.format(ans))

if all(ans2):
    print("You are correct")
else:
    print("Incorrect logic. Check your code")
# ###### CODE BLOCK TO DETERMINE WHETHER THE FUNCTION WORKS AS INTENDED ##### #

