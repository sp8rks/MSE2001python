# IMPORTS (YOU CAN ADD MORE IF NEEDED)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import os

from matplotlib.patches import Rectangle
import seaborn as sns


# %%

# =============================================================================
#     Q(example 0)
#        A basic plot of the equation y = x**2 + 3.
#        1. Add star markers
#        2. Make the line style (linestyle) doted (':')
#        3. Make the line color (color) blue.
#        4. Make the marker face color (mfc) transparent ('none').
#        5. Make the marker edge color (mec) "black"
#        6. Make the markers size (markersize) 15
#        7. Add tick markers to the top and right, make the direction "in"
#        8. DON'T FORGET TO "SHOW" YOUR RESULTS
# =============================================================================

########### THIS IS USEFUL! I AM SETTING THE GLOBAL FONT SIZE TO 14 ###########
plt.rcParams.update({'font.size': 14})
###############################################################################

plt.figure(figsize=(5,5))
x = np.arange(10)
y = x ** 2 + 3
plt.plot(x, y, '*', color='blue', linestyle=':', mfc='none', mec='k',
         markersize=15)
plt.tick_params(top=True, right=True, direction='in', length=10)
plt.ylabel('Total value')
plt.xlabel('Number of employees')
plt.savefig('example_figures/example0.png', bbox_inches='tight')
plt.show()


# %%
# =============================================================================
#     Q0 Plot "y = sin(x) + 2*tanh(x)" from x=-4 to x=4 with stepsize=0.1
#        1. Add circular markers
#        2. Make the line style (linestyle) dashed ('--')
#        3. Make the line color (color) maroon.
#        4. Make the marker face color (mfc) "white".
#        5. Make the marker edge color (mec) "black"
#        6. Add tick markers to the top and right, make the direction "in"
#           Make the ticks length 10
#        7. Set the xlim to (-4, 4), set the ylim to (-2, 3)
# =============================================================================









# %%
# =============================================================================
#     Q1 Plot the equation y = abs(exp(x) - x**(3))
#        0. Make the y-axis of the figure display on a log scale.
#         (change the figure, not your data)
#        1. Limit the x axis to values from -3, to 5.
#        2. Add a label to your data.
#        3. Add a legend to the bottom right. (figure this out)
#        4. Use square marker shapes.
#        6. Use a (non-boring) HEX color to set the marker face colors.
# =============================================================================








# %%
# =============================================================================
#     Q2 Plot three different equations to the same canvas.
#           50*sin(x), exp(x), x**2
#        1 . Make this look good. You are in charge of colors, linestyles,
#        markers, etc.
#        2. Please use different makers, colors, and lines for the different
#        data.
#        3. Label the three different lines and add a legend
# =============================================================================









# %%
# =============================================================================
#     Q3 Plot 2 XRD signals from the previous homework (you can find the data
#        and copy to a location where you can use it)
#        1. Make it look good. Eg. pleasant colors, tick marks facing in,
#        good axis, well-labeled, etc.
#        2. Add labels to each line (these don't have to be meaningful)
#        3. Look at the xaxis in range 10 eg. "xlim(3,13)". Make it interesting
#        4. Make sure you have x and y axis labels
# =============================================================================












# %%
# =============================================================================
#     Q4 Time to use subplots.
#        1. Make a histogram for each of your 2 XRD signals on one subplot
#        2. Make a histogram for the log XRD signals on the other subplot
#        3. Stack these plots one on top of another vertically.
#           That is, two rows, 1 column.
#        4. Make them look good using the same principles from above.
#           (consistent color schemes between plots, labeling, nice axes, etc.)
#        5. Make the histogram boxes outlined in black.
#        6. Make the boxes slightly transparent (maybe alpha=0.8ish)
#        7. Add enough bins that it looks good.
#
#           You will now need to work with "plt.axes". You can do all the same
#           things, but you might need to do it in a different way. For example
#           plt.ylabel() is now done on a per-axis basis using
#           axes[i].set_ylabel(). When in doubt search
#           "stuff I want to do" plus the library "matplotlib"
# =============================================================================













# %%
# =============================================================================
#     Q5 You will now be tasked with using gridspec. Take the two XRD signals
#        you were working with. On a single canvas use gridspec to make 3 axes.
#           - The axis (1) should have your xrd signal with a box around an
#           "interesting" part.
#           - The axis (2) should have should be the "zoomed" in location.
#           - The axis (3) should be the difference between the two signals
#           at the zoomed in location. An example is shown with the homework.
# =============================================================================















# %%
# =============================================================================
#     Q6-9 Generate 4 different plots of your choosing. Make them look good!
#          Follow the basic design principles I talked about.
#          One of the figures must be plotted against dates or times as the 
#          x axis.
#          SAVE ONE OF THESE FIGURES AS A PNG! Make sure it has the following
#              DPI=300, and bbox_inches='tight' (plt.savefig is the command)
# =============================================================================
