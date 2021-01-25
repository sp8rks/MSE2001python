# No imports are necessary for this assignment.
# You are welcome to use them though!


# %%
# =============================================================================
#     Q1: Demonstrate the ability to create varibles of different types
# =============================================================================

# float


# int


# complex


# string


# boolean


# %%
# =============================================================================
#     Q2: fill in the dictionary "data_type_dict".
# The "key" is the variable number.
# The associated value will be the variable type writen as a string
# =============================================================================
variable_0 = ('This' + 'is', 1, 'example of a tuple with mixed', {'variable': 'types'})
variable_1 = 'hello'
variable_2 = 5+3j
variable_3 = [False]
variable_4 = ['there',
              'is',
              'plenty',
              'of',
              'room',
              'at',
              'the',
              'bottom']
variable_5 = {'dalmatians': 101}
variable_6 = True
variable_7 = 911
variable_8 = tuple(variable_4)
variable_9 = {'key': 'value'}
variable_10 = 3.14159

variable_types = [int, float, complex, str, dict, tuple, list, bool]

data_type_dict = {0: 'tuple',  # variable_0 is a "tuple"
                  1: 'str',  # variable_1 is a "str"
                  2: 'FILL IN',
                  3: 'FILL IN',
                  4: 'FILL IN',
                  5: 'FILL IN',
                  6: 'FILL IN',
                  7: 'FILL IN',
                  8: 'FILL IN',
                  9: 'FILL IN',
                  10: 'FILL IN',
                  }


# %%
# =============================================================================
#     Q3: Figure out how to determine the type of a variable using python code
# The variable explorer does not count.
# =============================================================================



# %%
# =============================================================================
#     Q4: Demonstrate an ability to work with lists
# =============================================================================
# append items to a list


# add lists together


# get item from list using indexing


# slice list using postitive list indicies


# slice list using negative list indicies


# slice list using a positive AND negative list index


# Explain the "IndexError" produced by this code and FIX IT:
#example_list = ['113n', 1, 2.5, 15, 'dial', 155] #  (uncomment line and run)
#example_list[-15] #  (uncomment line and run)
your_explanation = '''
You can put your explanation here.
It can even go onto the next line :D
Please keep it short.
'''

# Explain why this code does not produce the same result.
# hint: see the error in the next problem if you don't know.
example_list[-15:]
your_explanation = '''
You can put your explanation here.
It can even go onto the next line :D
Please keep it short.
'''

# Explain the "TypeError" produced by this code and FIX IT:
example_list[1.0] #  (uncomment line and run)
your_explanation = '''
You can put your explanation here.
It can even go onto the next line :D
Please keep it short.
'''


# %%
# =============================================================================
#     Q5: Demonstrate an ability to work with strings
# =============================================================================
# add strings together


# show a string split


# show string indexing


# use string methods and indexing to extract information from the "info_string"
info_string = 'ADDRESS: 736 West North Temple, City: Salt Lake City, State: Utah, ZIP: 84116'
# your list should be of form [address, city, state, zip]
# use string.split or other string methods!
# comment: if you use regular expressions (regex) this is super easy. 
# bonus point if you figure (and kind of understand) a solution using regex.
info_list = 'your code here'  # eg info_string.split('your_str')[i].split('your_str')[j]


# string slice


# Explain the "SyntaxError" produced by this code and FIX IT:
# TAKE NOTE: YOU WILL PROBABLY GET THIS ERROR OFTEN! Mine still does. :P
#"Then I wrote this sentance #  (uncomment line and run)
your_explanation = '''
You can put your explination here.
It can even go onto the next line :D
Please keep it short.
'''


# %%
# =============================================================================
#     Q6: Use string formating to display the value of a float variable
# =============================================================================

# Display the value of both wavelenth and energy at two (2.00) decimal places

h = 4.135e-15  # this value of h will give output in electron volts (eV)
c = 3e8  # speed of light in meters/second
lambda_ = 525e-9  # wavelength of light in meters
energy = h * c / lambda_  # output in eV

# Print out a string that says:
'''
The energy of light given a wavelength of {wavelength} nm is approximately {energy} eV.
'''

# hint: look at the thread here.
# https://stackoverflow.com/questions/6149006/display-a-float-with-two-decimal-places-in-python


# %%
# =============================================================================
#     Q7: Demonstrate an ability to work with numbers
# =============================================================================
# convert float into int


# demostrate add, subtract, multiply, divide, power, and root examples


# demonstrate use of the modulo operator


# show integer division


# start with 1.104 add 15, then divide the sum by 7.5
# raise your result to the power of 5
# print this value with 5 decimal places
print("the value, using correct string formating, goes here")

# divide this value by 3 and print the remainder
print("the remainder, using correct string formating, goes here")


# %%
# =============================================================================
#     Q8: Figure out how to make a useful dictionary
# ============================================================================
# build a dictionary
#     use the "run numbers" as the keys.
#     use tuple with "parameter values" (floats) as the values
file_names = ["run_1_oxygen_concentration_0.015_time_10_min_temp_353_K",
              "run_2_oxygen_concentration_0.15_time_15_min_temp_358_K",
              "run_3_oxygen_concentration_0.0015_time_20_min_temp_349_K",
              "run_4_oxygen_concentration_0.055_time_20_min_temp_350_K",
              "run_5_oxygen_concentration_0.005_time_20_min_temp_350_K"]


# %%
# =============================================================================
#      Q9-10: Solve 2 problems from another engineering class
# =============================================================================
# instead of using a calculator, use python to do the math for another class
# print the answers with the appropriate significant figures.

# problem 1


# problem 2


