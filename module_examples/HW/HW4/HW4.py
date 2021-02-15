# IMPORTS (YOU CAN ADD MORE IF NEEDED)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os



# %%
# =============================================================================
#     Q(example 0)
#        Read in a XRD file using pandas.
# =============================================================================
path_xrd = 'xrd_data/'
filename = 'tioga1_0-8.csv'
df_XRD = pd.read_csv(path_xrd+filename, header=None)

print(df_XRD.describe())


# %%
# =============================================================================
#     Q0 Read in all the different file types from folder "bunch_a_files"
# https://www.analyticsvidhya.com/blog/2017/03/read-commonly-used-formats-using-python/
# =============================================================================
path_files = 'bunch_a_files/'
# read in ".csv" file


# read in ".xlsx" (excel) file  # in anaconda terminal, "conda install xlrd"


# read in ".txt" file


# read in ".JSON" file


# read in and then show image file  (I like to use pyplot)


# read in the ".data" file.



# %%
# =============================================================================
#     Q1 You have been given a folder named "xrd_data". There are a seven
#        different CSV files with XRD measurements in this folder. Combine all
#        these into 1 single XRD file. The first column should have 2theta
#        values. The rest should be XRD signals. Name the Columns based on the
#        input files. Please name you columns so they can be tracked back to
#        the original file. For example, the first XRD signal from the
#        "tioga1_0-8.csv" file could be "0-8, 1". The second signal could be
#        "0-8, 2", etc.

#        >>>print(df_combined_XRDs.columns)
#        ['0-8, 0', '0-8, 1', '0-8, 2',...'90-120, 5']
#
#        Save this combined csv as "combined_XRDs.csv" in the "HW4" folder.
#        Do not save the index into the CSV.
#        Hint: start by just practicing adding one or two columns with new 
#        names to an existing dataframe. Then use a for loop to systematically
#        generate names for the new data columns.
# =============================================================================







# %%
# =============================================================================
#     Q2 Your colleague has sent some data for you to analyze. When you open
#        the zip file, you see he uses MatLab, and has sent you ".mat" files.
#        How uncivilized. FIGURE OUT HOW TO READ IN THIS DATA.
#
#        When you inspect the data you notice it is 3-dimensional, explaining
#        why he didn't just send you .csv files.
#        USING PYTHON:
#           1. Read in the three MatLab files.
#           2. Save all data into a compressed ".npz" format. Your file should
#              be named "vectors.npz" and saved into the "matlab_data" folder.
#           3. Load the npz file & load saved vectors. (find online examples)
#           4. You have been told the u, v, w are components of vectors which
#              point in x, y, z space respectively.
#              How many vectors are there total? Save you answer to a variable
#              named "number_of_vectors" in the function, then print it.
#           5. Your function should "return (u, v, w)"
# =============================================================================
# function name: read_matlab






# %%
# =============================================================================
#     Q3 The vectors lie evenly spaced on a grid. However no absolute
#        x, y, z coordinates were provided. You will create these
#        yourself. Save these arrays to variabls named "x" "y" and "z".
#           "x" : An array which contains the "x" coordinates for each vector
#           "y" : An array which contains the "y" coordinates for each vector
#           "z" : an array which contains the "z" coordinates for each vector
#        HINT: You might find "np.meshgrid" to be useful here.
# =============================================================================
# function name: get_grid




# %%
# =============================================================================
#     Q4 You'll want to visualize the data to make sure you haven't messed up.
#        Your colleague sent you an image titled "vortex.png". This image
#        represents a slice through the "z" dimension at the 64th layer.
#        Figure out how to make a "quiver plot" that looks similar to his.
#        (NOTE: you do not need to get the exact same slice. But it should
#        look similar)
# =============================================================================
# function name: visualize_vortex





# %%
# =============================================================================
#     Q5 You are tasked with programatically determining whether a "vortex"
#        center exists for each slice through the z axis.
#        Think of 3 ways you can solve this. Write a paragraph outlining each
#        approach. Select one approach and code it.
#        Have it so your code returns a list with 0's (no vortex) and 1's
#        (vortex) saying if the z slice has a vortex.
#
#        You do not need to get every vortex perfect. You just need to do okay.
#        I am looking for clever solutions and simple code.
# =============================================================================
# function name: assign_vortex_labels






# %%
# =============================================================================
#     Q6 There are another 3 folders with .mat files. The data will always
#        be formated u, v, w. You will always need to assign x, y, z values.
#        The number of vectors is not guaranteed to be the same. The sample is
#        not guaranteed to be in the center. Please make a function that can
#        1. take a folder name, read its content
#        2. read in the .mat files and save them as a sinle npz file
#        2. make x, y, z coordinates for all vectors
#        3. determine whether or not a slice has a vortex in it
#        4. return a list of 0's and 1's saying if the slice has a vortex.
#
#        "Example of a sample and its vectors"
#        > sample_1.3
#           > u.mat
#           > v.mat
#           > z.mat

#        YOU SHOULD ALREADY HAVE THE PARTS FOR THIS (except 1.).
# =============================================================================
# function name: label_sample





# %%
# =============================================================================
#     Q7 You have been assigned to data processing for the trial of a new
#        processing tool. You hope to provide accurate and early diagnostic of
#        sample failure. You have been given a file with sample Id numbers,
#        the filename for their process parameters and the sample label showing
#        whether the sample was a success (0) or the sample failed (1).
#
#        Your supervisor believes that some parameters are highly correlated
#        to the sample labels. As a first pass, he would like you check if the
#        Max parameters values are the same between samples labeled 0 and 1.
#
#        - For all failed samples, please indicate the average "Max" value
#        for all parameters.
#        - Do the same thing for the succesful samples.
#        - Please find which parameter the has the largest "mean-Max"
#        difference between labels.
# =============================================================================
# function name: check_mean



# %%
# =============================================================================
#     Q8 You are informed that a statistician is being
#        hired to look at the results. He would like you make a datasheet that
#        has a row for each sample, and a column for the max of each
#        parameter. He wants each cell to contain the maximum value for each
#        sample/parameter combination. A final column should be added that
#        contains sample labels. This should be saved as a ".csv" file named
#        'samples.csv'.
# =============================================================================
# function name: save_sample_features





# %%
# =============================================================================
#     Q9 You have been asked to visualize the kde distribution for both labels
#        along all parameters. Make a plot with all parameters on it that shows
#        the kde plot.
#        HINT: You should use seaborn.distplot(row_of_data, hist=False)
# =============================================================================
# function name: plot_distributions




