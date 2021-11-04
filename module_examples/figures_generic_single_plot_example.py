import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

plt.rcParams['font.size']=14

path = r'data_for_exercises/'
filename = r'generic_single_plot.csv'
df = pd.read_csv(path+filename)

x = df['x'].dropna()
y = df['y'].dropna()

x2 = df['x2'].dropna()
y2 = df['y2'].dropna()

x3 = df['x3'].dropna()
y3 = df['y3'].dropna()

#bodacious colors
colors=sns.color_palette("rocket",3)
#Ram's colors, if desired
seshadri = ['#c3121e', '#0348a1', '#ffb01c', '#027608', '#0193b0', '#9c5300', '#949c01', '#7104b5']
#            0sangre,   1neptune,  2pumpkin,  3clover,   4denim,    5cocoa,    6cumin,    7berry


#plot
fig = plt.figure(1, figsize=(5, 5))
plt.semilogx(x3, y3, linestyle='-', marker='^', label='ammonium perchlorate', color=colors[2], mfc='w', markersize=8) # plot data
plt.semilogx(x2, y2, linestyle='-', marker='s', label='iron oxide', color=colors[1], mfc='w', markersize=8) # plot data
plt.semilogx(x, y, linestyle='-', marker='o', label='aluminum', color=colors[0], mfc='w', markersize=8) # plot data

#plt.plot(x_fit, ffit(x_fit), linestyle='-', marker='None', label='fit', color=colors[0], markerfacecolor='white', markersize=8) # plot data

#plot params
plt.xlim([1,1e4])
plt.ylim([-0.5,16])
plt.minorticks_on()
plt.tick_params(direction='in',right=True, top=True)
plt.tick_params(labelsize=14)
plt.tick_params(labelbottom=True, labeltop=False, labelright=False, labelleft=True)
#xticks = np.arange(0, 1e4,10)
yticks = np.arange(0,16.1,4)

plt.tick_params(direction='in',which='minor', length=5, bottom=True, top=True, left=True, right=True)
plt.tick_params(direction='in',which='major', length=10, bottom=True, top=True, left=True, right=True)
#plt.xticks(xticks)
plt.yticks(yticks)


#plt.text(1,325, f'y={Decimal(coefs[3]):.4f}x$^3$+{Decimal(coefs[2]):.2f}x$^2$+{Decimal(coefs[1]):.2f}x+{Decimal(coefs[0]):.1f}',fontsize =13)


plt.xlabel(r'particle radii ($\mu m$)', fontsize=14) 
plt.ylabel(r'percent contribution',fontsize=14)  # label the y axis


plt.legend(fontsize=14)  # add the legend (will default to 'best' location)

plt.savefig('data_for_exercises/plotting/generic_plot.png', dpi=300,bbox_inches="tight")