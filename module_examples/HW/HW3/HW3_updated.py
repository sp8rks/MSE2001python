# IMPORTS
import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt


# %%
# =============================================================================
#     Q(example 0)
#        Make a function that can loop through a list and find the numbers that
#        are divisible by N.
# =============================================================================
# function name: find_multiples_of_N
def find_multiples_of_N(list_of_values, N):
    """
   Determine all numbers in a list that are divisible by some number N
   
    Parameters
    ----------
    list_of_values : list or array-like
        list we will check through
    
    N : int
        number we are checking for divisibility

    Returns
    -------
    multiple_of_N : list
        List containing the numbers from original list that are divisible by N

    """
    multiple_of_N = []
    for value in list_of_values:
        if value % N == 0:
            multiple_of_N.append(value)
    return multiple_of_N






# ###### CODE BLOCK TO DETERMINE WHETHER THE FUNCTION WORKS AS INTENDED ##### #
# data to test your equation
list_with_numbers = [1, 16, 2134, 23400, 2105, 1203, 12340, 123400, 1772, 17]
Qe0_my_ans = find_multiples_of_N(list_with_numbers, 6)
Qe0_ans = [23400]
if Qe0_my_ans == Qe0_ans:
    print('Qe0 is correct')
else:
    print('Check your code for Qe0')
# ###### CODE BLOCK TO DETERMINE WHETHER THE FUNCTION WORKS AS INTENDED ##### #


# %%
# =============================================================================
#     Q(example 1)
#        Write a function that returns a list containing the max, mean, and
#        standard deviation for any given list of data.
#        hint: Convert the list to a numpy array
# =============================================================================
# function name: get_summary_statistics
def get_summary_statistics(data_of_interest):
    """
   Compute several descriptive statistics for the data of interest.

    Parameters
    ----------
    data_of_interest : list or array-like
        Input data.

    Returns
    -------
    stats : list
        List containing the max, mean and standard deviation.
        stats = [max, mean, std]

    """
    data_of_interest = np.array(data_of_interest)
    maximum = data_of_interest.max()
    mean = data_of_interest.mean()
    std = data_of_interest.std()
    stats = [maximum, mean, std]
    return stats





# ###### CODE BLOCK TO DETERMINE WHETHER THE FUNCTION WORKS AS INTENDED ##### #
# data to test your equation
np.random.seed(1)  # seed random generator so data2 values are always the same
Qe0_data1 = [15, 12, 1249, 9, 12, 923, 11, 234, 234, 16, 12335, 126, 123, 164,
             16124, 1464, 183829, 12, 923, 1249, 9, 188, 0, 0, 0, 0, 0, 0, 12]
Qe0_data2 = np.random.randint(0, 15591, 144113)
Qe0_data3 = np.sin(range(1000))
Qe0_data4 = np.exp(-np.linspace(-1, 1, 50)**2) + 1

# your answers
Qe0_my_ans1 = get_summary_statistics(Qe0_data1)
Qe0_my_ans2 = get_summary_statistics(Qe0_data2)
Qe0_my_ans3 = get_summary_statistics(Qe0_data3)
Qe0_my_ans4 = get_summary_statistics(Qe0_data4)

# correct answers
Qe0_ans1 = [183829, 7561.137, 33504.7370]
Qe0_ans2 = [15590, 7806.514776598919, 4503.730370743348]
Qe0_ans3 = [1, 0, 0.707]
Qe0_ans4 = [2, 1.739, 0.2061]

my_answers = Qe0_my_ans1 + Qe0_my_ans2 + Qe0_my_ans3 + Qe0_my_ans4
answers = Qe0_ans1 + Qe0_ans2 + Qe0_ans3 + Qe0_ans4
if np.allclose(my_answers, answers, atol=1e-2):
    print('Example Qe1 is correct')
else:
    print('Check your code for Example Qe1')
# ###### CODE BLOCK TO DETERMINE WHETHER THE FUNCTION WORKS AS INTENDED ##### #


# %%
# =============================================================================
#     Q0 Write a function that loops through a list of numbers and returns the
#        square of the (number + 2) for each. ie [(1+2)**2, (2+2)**2, ...]
# =============================================================================
# function name: plus_two_squared





# %%
# =============================================================================
#     Q1 Do the same, but use numpy operations and make it a "1-liner"
# =============================================================================
# function name: plus_two_squared_numpy











# ###### CODE BLOCK TO DETERMINE WHETHER THE FUNCTION WORKS AS INTENDED ##### #
# data to test your equation
list_of_numbers = list(range(10))
Q0_my_ans = plus_two_squared(list_of_numbers)
Q1_my_ans = plus_two_squared_numpy(list_of_numbers)
answer = [4, 9, 16, 25, 36, 49, 64, 81, 100, 121]
if np.allclose(Q0_my_ans, Q1_my_ans) and np.allclose(answer, Q1_my_ans):
    print('Q0 and Q1 are correct')
else:
    print('Check your code for Q0 and Q1')
# ###### CODE BLOCK TO DETERMINE WHETHER THE FUNCTION WORKS AS INTENDED ##### #


# %%
# =============================================================================
#     Q2 Write a function that, given a user input, will "try" to convert the
#        input to "int" type. On "exception", if the user has not input an
#        integer value you should inform them the input was incorrect and
#        reprompt them.
#        HINT: use a while loop until they get it correct.
# =============================================================================
# function name: check_user_input







# ###### CODE BLOCK TO DETERMINE WHETHER THE FUNCTION WORKS AS INTENDED ##### #
# data to test your equation
input_str = 'Type an integer in here: '
Q2_my_ans = get_user_input(input_str)
if type(Q2_my_ans) is int:
    print('Q2 is correct')
else:
    print('Check your code for Q2')
# ###### CODE BLOCK TO DETERMINE WHETHER THE FUNCTION WORKS AS INTENDED ##### #


# %%
# =============================================================================
#     Q3 Python allows you to take in input from the user with the input() 
# function. Within a while loop, propmpt the user to enter some valid python 
# code. Use the Try/Except method to test their code; if it works, end the 
# while loop; if it doesn't, prompt them again. 
#hint: you can use the eval() function to evaluate a string as python code 

# =============================================================================









# %%
# =============================================================================
#     Q4 In MSE2010 you used a software called imageJ that allowed you to 
#       calculate the weight fraction of a two phase mixture by using the 
#       'histogram' function. In that approach you could select a threshold
#       value of grayscale and it would return the fraction above and below
#       that threshold.
#       
#       In this problem you will write a function that does the same thing!
#       Your task is to open the image 'Sn-Bi.bmp' and use numpy to determine 
#       the area fraction of the Sn vs Bi phases in the sample.
#       to import the image and do the thresholding you will find the numpy
#       class video helpful https://youtu.be/maa6VQU-0Do
#
#       don't forget to crop out the bottom part of the SEM image
# =============================================================================
# name the function threshold_tool
# make the input to your threshold tool a file name and a threshold value
# have the function return the percent of the black phase
# I suggest using the following libraries to read and plot the image
from skimage import io











# ###### CODE BLOCK TO DETERMINE WHETHER THE FUNCTION WORKS AS INTENDED ##### #
Q4_my_ans = threshold_tool('Sn-Bi.bmp',132)
if np.isclose(Q4_my_ans,54.8717,1):
    print('Q4 is correct')
else:
    print('Check your code for Q4')
# ###### CODE BLOCK TO DETERMINE WHETHER THE FUNCTION WORKS AS INTENDED ##### #


# %%
# =============================================================================
#     Q5 You have been given xrd data and need to remove the part of the signal
#     associated with the sample holder. The data is measured across 2theta
#     with the total signal, and the just the sample holder.
#     You need to remove the background signal. 
#     Please write a function that given an xrd returns an array with two
#     columns, twotheta and signal-background

#     TASK:
#     - Data is provided as three columns: 2theta & totalsignal & background.
#     - Write a function removes the background signal from the total signal.
#     - Take in a three column array as the argument.
#     - return the data as an array with two columns: twotheta & signal

# =============================================================================
# function name: remove_xrd_background








# ###### CODE BLOCK TO DETERMINE WHETHER THE FUNCTION WORKS AS INTENDED ##### #
xrd_array = pd.read_csv('xrd_csv_files/xray_with_background.txt',
                       delim_whitespace=True).values
corrected_xrd = remove_xrd_background(xrd_array)
twotheta = xrd_array[:, 0]
uncorrected = xrd_array[:, 1]
corrected = corrected_xrd[:, 1]
plt.plot(twotheta, uncorrected, label='with background signal')
plt.plot(twotheta, corrected, label='no background signal')
plt.legend()
plt.show()
if np.allclose(corrected[-3:], [60.799, 126.816, 130.834]):
    print('Q5 is correct')
else:
    print('Check your code for Q5')
# ###### CODE BLOCK TO DETERMINE WHETHER THE FUNCTION WORKS AS INTENDED ##### #

# %%
# =============================================================================
#     Q6 Researchers have generated structure data for Co3O4.
#     Measurement 1 was done using Neutron diffraction.
#     Measurement 2 was was done using the characterization labs XRD machine. 

#     This data needs to be transformed to "Q space" so that the measurements  
#     can be compared. You will make a function that performs this conversion.

#     TASK:
#     - Data are provided in as an array with two columns: 2theta & amplitude.
#     - Write a function that takes in 1. the data array and 2. the wavelength
#       used for the measurment.
#     - normalize the signal so that peaks can be compared.
#          (make the smallest y-value 0 & the largest y-value 1)
#     - return the data as an array with two columns: q_space & amplitude

# =============================================================================
# function name: get_Qspace











# ###### CODE BLOCK TO DETERMINE WHETHER THE FUNCTION WORKS AS INTENDED ##### #
xrd_file = 'xrd_csv_files/xray_with_background.txt'
neutron_file = 'xrd_csv_files/co3o4_RT_neutron.txt'
nuetron_data = pd.read_csv(neutron_file, delim_whitespace=True).values
xrd_w_background = pd.read_csv(xrd_file, delim_whitespace=True).values
xrd_data = remove_xrd_background(xrd_w_background)

neutron_wavelength = 2.5
xrd_wavelength = 1.7902

q_neutron = to_Qspace(nuetron_data, neutron_wavelength)
q_xrd = to_Qspace(xrd_data, xrd_wavelength)

plt.plot(q_neutron[:, 0], q_neutron[:, 1], label='neutron signal')
plt.plot(q_xrd[:, 0], q_xrd[:, 1], label='xrd signal')
plt.legend()
plt.show()

neutron_correct = np.allclose(q_neutron[:3, 0], [0.13991099, 0.14429572, 0.14868035])
xrd_correct = np.allclose(q_xrd[:3, 0], [0.97693038, 0.9779616, 0.97899281])
if neutron_correct and xrd_correct:
    print('Q6 is correct')
else:
    print('Check your code for Q6')
# ###### CODE BLOCK TO DETERMINE WHETHER THE FUNCTION WORKS AS INTENDED ##### #


# %%
# =============================================================================
#     Q7 Plastic deformation in single crystals occurs as a result of slip in 
# the crystal structure. In any slip system, slip begins at a critical shear 
# stress, tau_critical. This can be measured experimentally, but it is much 
# easier calculate the value for a give cyrstal structure.

# Consider a single crystal of BCC iron oriented so that a tensile stress is
# applied along a [010] direction. Compute the resolved shear stress along a 
# (110) plane and in a [-1,1,1] direction when a tensile stress of 52 MPa is 
# applied.

# The formula for crtical shear stress is:
# tau_cr = sigma * cos(phi) * cos(lambda)

# Where sigma is stress, phi is the angle between the tension and plane vectors,
# and lambda is the angle between the tension and slip vectors.

# =============================================================================
# name your function critical_shear_stress
# function should accept stress, load direction, direction normal to slip plane
# and slip direction as inputs and return a critical shear stress as output










# ###### CODE BLOCK TO DETERMINE WHETHER THE FUNCTION WORKS AS INTENDED ##### #
sigma_t = 52 # MPa
load_direction = np.array([0,1,0])
plane_direction = np.array([1,1,0])
slip_direction = np.array([-1,1,1])

tau_critical = critical_shear_stress (sigma_t, load_direction,
                           plane_direction, slip_direction)

if np.isclose(tau_critical, 21.22, 0.25):
    print("You got this problem correct!")
else: 
    print("Sorry, try again!")

# %%
# =============================================================================
#     Q8 Your lab has an old furnace. Your advisor thinks the furnace uses less
#        power when the building is warmer. Lets see if this is True.

#        ****Data is given in watts, please convert to kilowatts****
#        PART 1 ------- function name: mean_power_usage
#        First:
#            Determine the furnace's average power usage during the summer 
#            months (May, June, July, August) for each year it has been
#            running. The furnace runs for 8 hours a day.
#        Then:
#            Determine the average power usage during the winter 
#            (November, December, January, February) for each year it has been
#            running. The furnace runs for 8 hours a day.
#        Make a function that recieves the following arguments:
#            1. year (as an int)
#            2. months (as a list of ints eg. [1, 2, 3])

#       PART 2 ------- Showing your work, determine if there is a significant
#            difference in power usage (summer vs winter) during this furnaces
#            lifetime. 
#            "a significant difference" == power_summer <= (0.9 * power_winter)

#   Might be useful to know. The furnace runs EVERYDAY.
#   days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#   days_in_leap_year_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#   2014 was a leap year. Every 4 years is a leap year.
# =============================================================================
# function name: mean_power_usage
# hint: data is in the path: 'furnace_data/data'









# SELECT THE CORRECT ANSWER (delete one, keep the other)
significant_difference = True
significant_difference = False
# ####################################

# ###### CODE BLOCK TO DETERMINE WHETHER THE FUNCTION WORKS AS INTENDED ##### #
correct_function = mean_power_usage(2020, [1, 2, 3]) == 2635.5663263070364
if summer_avg <= 0.9 * winter_avg and correct_function:
    print('Q8 is correct')
else:
    print('Check your code for Q8')
# ###### CODE BLOCK TO DETERMINE WHETHER THE FUNCTION WORKS AS INTENDED ##### #


# %%
# =============================================================================
#     Q9 create an array in numpy representing your quizzes in the class so far
# The array should include your score per question (0 or 1) for each quiz.
# 
# Use this array and numpy functions to calculate teh following:
# (1) your average score per quiz,
# (2) your average score overall for the entire quiz category, and
# (3) the average score per question number (1-10)
# =============================================================================











