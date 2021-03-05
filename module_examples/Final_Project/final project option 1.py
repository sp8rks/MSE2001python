# IMPORTS (YOU CAN ADD MORE IF NEEDED)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import fsolve, minimize, curve_fit
from scipy.integrate import odeint
import pint
import scipy.constants as cnst
from molmass import Formula

# FINAL PROJECT
# For the final project in this class, you are assigned to create a python 
# version of the software ChemSolve v 1.2 built by the one and only Prof McQueen
# This tool is really helpful when synthesizing materials. It's a great tool to 
# double check your stoichiometry math.
# Check the tool out here https://occamy.chemistry.jhu.edu/chemsolve/index.php


# Your python module should prompt the user to input the desired target Formula,
# a list of the starting materials, a list of elements or compounds that can be 
# ignored and do not need to be balanced (such as oxygen or nitrogen coming from
# air, or the ability to "burn off" carbon in carbonate groups etc), and the 
# total quantity of desired starting materials or final product in milligrams.

# If you haven't taken general chemistry yet and are unfamiliar with stoichiometric
# calculations, let Prof Sparks know and he will find a solution for your
# situation