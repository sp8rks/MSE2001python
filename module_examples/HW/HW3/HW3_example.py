# IMPORTS
import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt


# ASSIGNMENT 3 (Week 3, Loop and arrays)
# =============================================================================
# I have defined a student "class". This outlines what a student object is.
# You don't need to worry about this part!!!
class Student():
    def __init__(self, first_name, last_name, u_id, email):
        self.assignment = 3
        self.description = "HW3, Loops and Arrays"
        self.due_date = "January 26, 2020"
        self.first_name = first_name
        self.last_name = last_name
        self.u_id = u_id
        self.email = email
        self.HWScores = {}

    def get_final_score(self):
        self.final_score = 0
        for score in self.HWScores.values():
            self.final_score += score
        return self.final_score


# FILL THIS OUT SECTION SO IT IS EASY FOR ME TO AUTO GRADE THINGS.
student = Student(first_name='first', last_name='last',
                  u_id='uXXXXXXX', email='email@email.com')
# =============================================================================


# %%
# =============================================================================
#     Q(example 0)
#        Make a function that can loop through a list and find the numbers that
#        are divisible by N.
# =============================================================================
# function name: find_multiples_of_N
def find_multiples_of_N(list_of_values, N):
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
    student.HWScores['Qe0'] = 0.2  # add score for correct execution
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
    student.HWScores['Qe1'] =  0.2  # add score for correct execution
else:
    print('Check your code for Example Qe1')
# ###### CODE BLOCK TO DETERMINE WHETHER THE FUNCTION WORKS AS INTENDED ##### #


# %%
# =============================================================================
#     Q0 Write a function that loops through a list of numbers and returns the
#        square + 2 for each of them. ie [1**2 + 2, 2**2 + 2, ...]
# =============================================================================
# function name: squared_plus_two
def squared_plus_two(list_of_numbers):
    squared_list = []
    for number in list_of_numbers:
        squared_list.append(number**2 + 2)
    return squared_list


# %%
# =============================================================================
#     Q1 Do the same, but use numpy operations and make it a "1-liner"
# =============================================================================
# function name: squared_plus_two_numpy
def squared_plus_two_numpy(list_of_numbers):
    squared_list = list(np.array(list_of_numbers)**2 + 2)
    return squared_list


# ###### CODE BLOCK TO DETERMINE WHETHER THE FUNCTION WORKS AS INTENDED ##### #
# data to test your equation
list_of_numbers = list(range(10))
Q0_my_ans = squared_plus_two(list_of_numbers)
Q1_my_ans = squared_plus_two_numpy(list_of_numbers)
answer = [2, 3, 6, 11, 18, 27, 38, 51, 66, 83]
if np.allclose(Q0_my_ans, Q1_my_ans) and np.allclose(answer, Q1_my_ans):
    print('Q0 and Q1 are correct')
    student.HWScores['Q0 & Q1'] = 2  # add score for correct execution
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
def get_user_input(input_str):
    int_type = False
    while not int_type:
        user_input = input(input_str)
        try:
            user_input = int(user_input)
            int_type = True
        except ValueError:
            print('incorrect input type.\n')
    return user_input


# ###### CODE BLOCK TO DETERMINE WHETHER THE FUNCTION WORKS AS INTENDED ##### #
# data to test your equation
input_str = 'Type an integer in here: '
Q2_my_ans = get_user_input(input_str)
if type(Q2_my_ans) is int:
    print('Q2 is correct')
    student.HWScores['Q2'] = 1  # add score for correct execution
else:
    print('Check your code for Q2')
# ###### CODE BLOCK TO DETERMINE WHETHER THE FUNCTION WORKS AS INTENDED ##### #


# %%
# =============================================================================
#     Q3 Create a function that thinks of a number and makes you guess it.
#        This should run until you guess correctly.
#        HINT: use a while loop until the guess is correct.
# =============================================================================
# function name: normalize_XRDs
def guess_my_number(lower=0, upper=5):
    # use numpy to generate a random integer in range "lower" and "upper"
    number = np.random.randint(lower, upper)
    guessed_correct = False
    while guessed_correct is False:
        # guess a number
        message_to_user = f'Please guess a number: '
        user_input = get_user_input(message_to_user)
        if user_input > number:
            print('You guessed too high')
        elif user_input < number:
            print('You guessed too low')
        else:
            print(f'Nice. My number is {number:0.0f}.')
            guessed_correct = True
    return True


# ###### CODE BLOCK TO DETERMINE WHETHER THE FUNCTION WORKS AS INTENDED ##### #
# data to test your equation
Q3_my_ans = guess_my_number()
if Q3_my_ans:
    print('Q3 is correct')
    student.HWScores['Q3'] = 1  # add score for correct execution
else:
    print('Check your code for Q3')
# ###### CODE BLOCK TO DETERMINE WHETHER THE FUNCTION WORKS AS INTENDED ##### #


# %%
# =============================================================================
#     Q4 The given XRD data is presented with raw machine values save as a CSV.
#        The "count" needs to be normalized for proper ploting.
#
#        Create a function that will normalize the XRD data so that the max
#        point across all XRD plot has a value of 1.
#
#        Your function should take in a numpy array and return a numpy array.
#        The return array shoule be normalized.
#        Your function should adhear to the provided """docstring""".
#
#
#        Data Description:
#        "The clay fraction from seven horizons was analyzed by XRD, using the
#        five common treatments: potassium saturation (K), potassium saturation
#        heated to 350 Deg C (K 350), potassium saturation heated to 550 Deg C
#        (K 550), magnesium saturation (Mg), and magnesium + glycerin
#        saturation (Mg+GLY)."
#
#        https://casoilresource.lawr.ucdavis.edu/software/r-advanced-statistical-package/plotting-xrd-x-ray-diffraction-data/
# =============================================================================
# function name: normalize_XRD
def normalize_XRD(xrd_signal):
    """
    normalize XRD singal

    Parameters
    ----------
    xrd_signal : array_like of size (N x 2)
        2D Signal information regarding XRD measurement where N is the number
        of signal measurements. The input file should have two columns. The
        first column contains data regarding 2theta.The second columns needs to
        have the signal amplitude.

    Returns
    -------
    normalized_xrd_signal : array_like of size (N x 2)
        A max-normalized XRD signal corresponsing to the input XRD.

    """
    normalized_xrd_signal = xrd_signal.copy()
    normalized_xrd_signal[:, 1] = xrd_signal[:, 1] / xrd_signal[:, 1].max()
    return normalized_xrd_signal


# ###### CODE BLOCK TO DETERMINE WHETHER THE FUNCTION WORKS AS INTENDED ##### #
# read in the XRD data and extract numpy values.
# Note: pandas columns would also work. But lets work with numpy for now.
xrd_signal = pd.read_csv('XRD1.csv').values
# pd.read_csv('XRD1.csv').plot()
# get the normalized values
Qe4_my_ans = normalize_XRD(xrd_signal)

# plot the data. The rows and columns can be accessed with slicing/indexing.
# array_like[rows, columns]. Grab all ":" of the rows for the column "0" or "1"
plt.plot(Qe4_my_ans[:, 0], Qe4_my_ans[:, 1])
plt.xlabel('2$\\theta$')
plt.ylabel('Signal, Arbitrary Units (A.U.)')
plt.tick_params(top=True, right=True, direction='in')
plt.show()

# check that the data is propely normalized.
if max(Qe4_my_ans[:, 1]) == 1:
    print('Q4 is correct')
    student.HWScores['Q4'] = 1  # add score for correct execution
else:
    print('Check your code for Q4')
# ###### CODE BLOCK TO DETERMINE WHETHER THE FUNCTION WORKS AS INTENDED ##### #


# %%
# =============================================================================
#     Q5 Additional XRD data has been collected. This data again needs to
#     normalized. Write a function that globaly normalizes the curves. That is
#     to say, make it such that the max value from ALL XRD measurements is 1.
# =============================================================================
# function name: normalize_XRDs
def normalize_XRDs(xrd_signals):
    """
    normalize XRD singal

    Parameters
    ----------
    xrd_signals : array_like of size (N x M)
        2D Signal information regarding XRD measurement where N is the number
        of signal measurements, and M the number of columns. The first column
        should contain data regarding 2theta.The remaining columns need to
        have the signal amplitudes which will be compared.

    Returns
    -------
    normalized_xrd_signal : array_like of size (N x 2)
        A max-normalized XRD signal corresponsing to the input XRD.

    """
    normalized_xrd_signals = xrd_signals
    signals = xrd_signals[:, 1:]
    max_reading = xrd_signals[:, 1:].max()
    normalized_xrd_signals[:, 1:] = signals / max_reading
    return normalized_xrd_signals


# ###### CODE BLOCK TO DETERMINE WHETHER THE FUNCTION WORKS AS INTENDED ##### #
# read in the XRD data and extract numpy values.
# Note: pandas columns would also work. But lets work with numpy for now.
xrd_signals = pd.read_csv('XRD.csv').values

# get the normalized values
Qe5_my_ans = normalize_XRDs(xrd_signals)

# plot the data. The rows and columns can be accessed with slicing/indexing.
# array_like[rows, columns]. Grab all ":" of the rows for the column "0" or "1"
plt.plot(Qe5_my_ans[:, 0], Qe5_my_ans[:, 1:])
plt.xlabel('2$\\theta$')
plt.ylabel('Signal, Arbitrary Units (A.U.)')
plt.tick_params(top=True, right=True, direction='in')
plt.show()

# check that the data is propely normalized.
if max(Qe5_my_ans[:, 1]) == 1:
    print('Q5 is correct')
    student.HWScores['Q5'] = 1  # add score for correct execution
else:
    print('Check your code for Q5')
# ###### CODE BLOCK TO DETERMINE WHETHER THE FUNCTION WORKS AS INTENDED ##### #


# %%
# =============================================================================
#     Q6 Your superior has an interest in finding all maximum peak values.
#
#        For each XRD signal, they want you to extract the globaly NORMALIZED
#        value and 2theta representing the signals highest peak.
#
#        Only consider signal values between 2theta=5 and 2theta=30.
#
#        Given an array that contains all XRD runs, return (for each run) the
#        2theta value and the corresponding normalized signal value.
#
#        HINT: I searched "numpy get location of max value"
# =============================================================================
# function name: get_XRD_peaks
def get_XRD_peaks(all_xrd_signals):
    all_xrd_signals = all_xrd_signals.copy()
    global_max = all_xrd_signals[:, 1:].max()
    theta_less_5 = all_xrd_signals[:, 0] < 5
    theta_greater_30 = all_xrd_signals[:, 0] > 30
    all_xrd_signals[theta_less_5] = -1e6
    all_xrd_signals[theta_greater_30] = -1e6

    peak_info = []
    for signal in all_xrd_signals.T:
        max_idx = np.argmax(signal)
        max_two_theta = all_xrd_signals[:, 0][max_idx]
        max_val = signal[max_idx]
        peak_info.append([max_two_theta, max_val/global_max])

    return peak_info


# ###### CODE BLOCK TO DETERMINE WHETHER THE FUNCTION WORKS AS INTENDED ##### #
# read in the XRD data and extract numpy values.
# Note: pandas columns would also work. But lets work with numpy for now.
all_xrd_signals = pd.read_csv('all_XRD.csv').values
Qe6_my_ans = get_XRD_peaks(all_xrd_signals)
Qe6_ans = [[30.0, 0.01946787800129786],
           [6.24, 0.2517845554834523],
           [6.32, 0.2673588578844906],
           [6.4, 0.1862426995457495],
           [8.72, 0.20765736534717716],
           [8.76, 0.372485399091499],
           [30.0, 0.01946787800129786],
           [8.68, 0.17975340687865024],
           [7.56, 0.11486048020765736],
           [8.72, 0.09149902660609993],
           [8.76, 0.136275146009085],
           [8.8, 0.15963659961064244],
           [30.0, 0.01946787800129786],
           [6.28, 0.7508111615833875],
           [6.36, 0.6969500324464634],
           [6.4, 0.45295262816353016],
           [7.8, 0.21414665801427643],
           [8.24, 0.3614536015574302],
           [30.0, 0.01946787800129786],
           [8.52, 0.20571057754704739],
           [8.64, 0.19402985074626866],
           [8.52, 0.12199870214146658],
           [8.6, 0.15574302401038287],
           [8.64, 0.3036988968202466],
           [30.0, 0.01946787800129786],
           [8.64, 0.24853990914990265],
           [7.64, 0.16677482154445167],
           [8.6, 0.30045425048669694],
           [8.76, 0.6216742375081116],
           [8.6, 1.0],
           [30.0, 0.01946787800129786],
           [6.24, 0.37637897469175857],
           [6.28, 0.2900713822193381],
           [6.4, 0.23880597014925373],
           [8.64, 0.1700194678780013],
           [8.64, 0.35236859182349123],
           [30.0, 0.01946787800129786],
           [8.76, 0.3309539260220636],
           [8.68, 0.2336145360155743],
           [8.68, 0.25762491888384165],
           [8.72, 0.47112264763140815],
           [8.72, 0.5827384815055159]]

global_max = all_xrd_signals[:, 1:].max()
plt.plot(all_xrd_signals[:, 0], all_xrd_signals[:, 1:] / global_max, alpha=0.5)
two_theta = [ans[0] for ans in Qe6_my_ans]
peak_values = [ans[1] for ans in Qe6_my_ans]
plt.plot(two_theta, peak_values, 'ks', alpha=0.4, mfc='r')
plt.xlabel('2$\\theta$')
plt.ylabel('Signal, Arbitrary Units (A.U.)')
plt.tick_params(top=True, right=True, direction='in')
plt.show()


all_signals_match = np.allclose(Qe6_my_ans, Qe6_ans)
# check that the data is propely normalized.
if all_signals_match:
    print('Q6 is correct')
    student.HWScores['Q6'] = 1  # add score for correct execution
else:
    print('Check your code for Q6')
# ###### CODE BLOCK TO DETERMINE WHETHER THE FUNCTION WORKS AS INTENDED ##### #


# %%
# =============================================================================
#     Q7  You have
#        been given an example of the "power usage" file. Please read this file
#        to get the average power requirement for a furnace run in "watts".
#
#        Make a function to take in a files path, then return the average watts
#
#        HINT: the file path is given, but you will need to figure out how to
#        read in a .txt file. You will then need to parse this file to get the
#        average watts required for a run.
# =============================================================================
# function name: extract_power_usage
def extract_power_usage(file_path):
    watt_usage = np.loadtxt(file_path)
    avg_usage = watt_usage.mean()
    return avg_usage


# ###### CODE BLOCK TO DETERMINE WHETHER THE FUNCTION WORKS AS INTENDED ##### #
file_path = 'furnace_data/data/power_usage_1990_2_13.txt'
Qe7_my_ans = extract_power_usage(file_path)
Qe7_ans = 3849.83

if np.isclose(Qe7_my_ans, Qe7_ans, atol=5):
    print('Q7 is correct')
    student.HWScores['Q7'] = 1  # add score for correct execution of exmpl Q0
else:
    print('Check your code for Q7')
# ###### CODE BLOCK TO DETERMINE WHETHER THE FUNCTION WORKS AS INTENDED ##### #


# %%
# =============================================================================
#     Q8 You have been asked to go through all the old furnace data to
#        determine how badly the furnace has diverged from its original
#        performance.
#
#        As a first step, determine the furnace's average power usage (kW hr)
#        for each year it has been running. The furnace runs for 8 hours.
#
#        Make a function that recieves the "data directory" as an argument, and
#        saves the mean power usage as a dictionary. For each year you will
#        have:
#            1. The year (type=int) as your key and
#            2. The years mean power (type=float) as the values.
#               eg. my_dictionary[int(year)] = float(mean_power)
# =============================================================================
# function name: yearly_mean_power_usage
def yearly_mean_power_usage(data_directory):
    files = os.listdir(data_directory)
    yearly_power_usage = {}
    years = range(1990, 2019)
    for year in years:
        yearly_run_info = np.zeros(0)
        for file in files:
            if str(year) in file:
                file_path = data_directory + file
                # year = int(file.split('_')[2])
                yearly_run_info = np.concatenate([yearly_run_info,
                                                  np.loadtxt(file_path)])
                kw_yearly_run_info = yearly_run_info / 1000  # convert to KW
                kw_hr_kw_yearly_run_info = kw_yearly_run_info * 8  # get hrs
        yearly_power_usage[year] = kw_hr_kw_yearly_run_info.mean()
    return yearly_power_usage


# ###### CODE BLOCK TO DETERMINE WHETHER THE FUNCTION WORKS AS INTENDED ##### #
data_directory = 'furnace_data/data/'
Qe8_my_ans = yearly_mean_power_usage(data_directory)
Qe8_ans = {1990: 30.876916303979954,
           1991: 31.06992361812489,
           1992: 31.20071347237487,
           1993: 31.39171270040579,
           1994: 31.672418028663692,
           1995: 31.594351355272504,
           1996: 31.7317559830578,
           1997: 31.77661432509812,
           1998: 31.937056701026947,
           1999: 32.16094319909025,
           2000: 32.16950441499824,
           2001: 32.45852805113597,
           2002: 32.60904833953194,
           2003: 32.573403883163635,
           2004: 32.756831685461805,
           2005: 32.83613488301028,
           2006: 32.793876725590835,
           2007: 33.065052571734654,
           2008: 33.348297490218805,
           2009: 33.255843127728085,
           2010: 33.68263366889195,
           2011: 33.84635129764068,
           2012: 33.87913383916766,
           2013: 34.2412791133325,
           2014: 34.163911456355514,
           2015: 34.48388092909946,
           2016: 34.42839220751652,
           2017: 34.381747192549014,
           2018: 34.67648718452646}

plt.plot(list(Qe8_my_ans.keys()), list(Qe8_my_ans.values()))
plt.xlabel('Year')
plt.ylabel('Average kiloWatt-hrs per run')
plt.tick_params(top=True, right=True, direction='in')
plt.show()

Qe8_my_ans_array = np.array(list(Qe8_my_ans.values()))
Qe8_ans_array = np.array(list(Qe8_ans.values()))

if np.allclose(Qe8_my_ans_array, Qe8_ans_array):
    print('Q8 is correct')
    student.HWScores['Q8'] = 1  # add score for correct execution
else:
    print('Check your code for Q8')
# ###### CODE BLOCK TO DETERMINE WHETHER THE FUNCTION WORKS AS INTENDED ##### #


# %%
# =============================================================================
#     Q9 Your manager believes that a new furnace would be cheaper
#        when considering the power usage over the next 25 years. The furnances
#        always run for 8 hours every day of the year (365 days).
#
#        The cost of a new furnace is $7,000. It will use 15 kWhrs / run.
#        The cost of energy is $0.25 / kilowatt-hour.
#
#        Determine whether a new furnace should be purchased if the furnace
#        continues to follow its current trend regarding power usage.
#
#        Step 1: Determine how many kilowatt hours the new furnace will use
#        over the next 15 years.
#
#        Step 2: Determine how many killowatt hours the old furnace will use
#        over the next 15 years. You can use your previous answer to determine
#        the slope and intercept if needed.
#
#        Step 3: Determine the difference in cost between running the two
#        furnaces.
#
#        Does this justify purchasing a new furnace (y/n/"too close to say")?
# =============================================================================
# ############# Step 1 ############# #
cost = 7000
cost_kwh = 0.25
kW_hours_needed_to_justify = cost/cost_kwh
runs_per_year = 365
total_runs = runs_per_year * 15  # runs
new_furnace_usage = 25  # kWhrs / run


# ############# Step 2 ############# #
# figure out best fit on the data.
m = (Qe8_my_ans[2018] - Qe8_my_ans[1990]) / (2018 - 1990)
b = Qe8_my_ans[2018] - m * 2018


# get equation for calculating watt usage at any future year.
def get_kWatt_usage(year):
    watt_usage = m * year + b
    return watt_usage

# kilowatt hours over next 15 years.
# looped solution
old_furnace_kwhrs = 0
for year in range(2019, 2019 + 15):
    average_kwhr_per_run = get_kWatt_usage(year)  # kwhr/run
    this_years_kwh_usage = average_kwhr_per_run * runs_per_year
    old_furnace_kwhrs = old_furnace_kwhrs + this_years_kwh_usage


# geometric solution
delta_y = get_kWatt_usage(2019 + 15) - get_kWatt_usage(2019)
delta_x = 15
old_furnace_kwhrs = (delta_y * delta_x) / 2 + delta_x * get_kWatt_usage(2019) * 365


# ############# Step 3 ############# #
new_furnace_kwhrs = total_runs * new_furnace_usage
delta_kwhrs = old_furnace_kwhrs - new_furnace_kwhrs

# if delta_kwhrs < kW_hours_needed_to_justify:
#     print('old furnace is fine')
# else:
#     print('new furnace will save $$$ over 15 years')


# ###### CODE BLOCK TO DETERMINE WHETHER THE FUNCTION WORKS AS INTENDED ##### #
should_they_buy_furnace = 'y'
if should_they_buy_furnace.lower() == 'y':
    print('Q9 is correct')
    student.HWScores['Q9'] = 1  # add score for correct execution
else:
    print('Check your code for Q9')
# ###### CODE BLOCK TO DETERMINE WHETHER THE FUNCTION WORKS AS INTENDED ##### #


# %%
# =============================================================================
#     Q10 Find the eigen values, and eigen vectors for the following matrices.
#         Use numpy operations for a quick 1-line solution.
# =============================================================================

matrix_1 = np.array([[1, 3, 4], [2, 1, 4], [1, 1, 1]])
matrix_2 = np.array([[1, 1, 2], [2, 5, 3], [5, 2, 3]])

# w, v = "you solution returns these"
w, v = np.linalg.eig([matrix_1, matrix_2])

# ###### CODE BLOCK TO DETERMINE WHETHER THE FUNCTION WORKS AS INTENDED ##### #
if w is not None and v is not None:
    print('Q10 is correct')
    student.HWScores['Q10'] = 1  # add score for correct execution
else:
    print('Check your code for Q10')
# ###### CODE BLOCK TO DETERMINE WHETHER THE FUNCTION WORKS AS INTENDED ##### #

# %%

expected_score = student.get_final_score()
print(f'your expected score for HW3 is {expected_score:0.0f}/10')
