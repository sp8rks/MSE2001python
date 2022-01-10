import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np
import matplotlib as mpl
import seaborn as sns
mpl.rcParams['pdf.fonttype'] = 42
mpl.rcParams['font.size']=14

#grab dataset 
filename = r'data_for_exercises/spectroscopy.csv'
df = pd.read_csv(filename)

#downsample data to every 10th data point
df = df.iloc[::10, :]

#pull data from CSV
x90 = df['X 90 Kohm'].dropna()
y90 = df['Y 90 Kohm'].dropna()
x90_clear = df['X 90 Kohm-clear'].dropna()
y90_clear = df['Y 90 Kohm-clear'].dropna()
x60 = df['X 60 Kohm'].dropna()
y60 = df['Y 60 Kohm'].dropna()
x60_clear = df['X 60 Kohm-clear'].dropna()
y60_clear = df['Y 60 Kohm-clear'].dropna()
x30 = df['X 30 Kohm'].dropna()
y30 = df['Y 30 Kohm'].dropna()
x30_clear = df['X 30 Kohm-clear'].dropna()
y30_clear = df['Y 30 Kohm-clear'].dropna()

#Set the limits of the plot for dataset1
xmin=400
xmax=800
ymin=60
ymax=120


#Generate some nice colors
seshadri = ['#c3121e', '#0348a1', '#ffb01c', '#027608', '#0193b0', '#9c5300', '#949c01', '#7104b5']
#            0sangre,   1neptune,  2pumpkin,  3clover,   4denim,    5cocoa,    6cumin,    7berry
#Or try a color from seaborn
colors=sns.color_palette("rocket",6)



#Prepare multipanel plot 
fig = plt.figure(1, figsize=(5, 5))
gs = gridspec.GridSpec(4,4)
gs.update(wspace=0.2, hspace=0.25)

#Generate first panel
#remember, the grid spec is rows, then columns
xtr_subsplot= fig.add_subplot(gs[0:4,0:2])

#plot data for left panel
plt.plot(x90, y90, linestyle='none', marker='^', label='90', 
         color=colors[0], mfc='w', markersize=8)
plt.plot(x60, y60, linestyle='none', marker='o', label='60', 
         color=colors[1], markerfacecolor='w', markersize=8)
plt.plot(x30, y30, linestyle='none', marker='s', label='30', 
         color=colors[2], markerfacecolor='w', markersize=8)

#Define where you want ticks
xticks = np.arange(0,(xmax+1),(xmax/4))
yticks = np.arange(ymin,(ymax+1),(ymax/4))

#or do xticks by hand if they don't look right
xticks = np.arange(300,701,200)
yticks = np.arange(60,121,20)


#provide info on tick parameters
plt.minorticks_on()
plt.tick_params(direction='in',which='minor', length=5, 
                bottom=True, top=True, left=True, right=True)
plt.tick_params(direction='in',which='major', length=10, 
                bottom=True, top=True, left=True, right=True)
plt.xticks(xticks)
plt.yticks(yticks)

#create a legend
plt.legend()

#plot limits
plt.xlim(xmin,xmax)
plt.ylim(ymin,ymax)


#Create axes labels
plt.ylabel(r'Transparency % $\alpha$')  
#plt.xlabel('Wavelength (nm)')
plt.text(645,52,'Wavelength (nm)')

#generate second panel
xtr_subsplot = fig.add_subplot(gs[0:2,2:4])
plt.plot(x90_clear, y90_clear, linestyle='none', marker='^', 
         label='90 clear', color=colors[3], mfc='w', markersize=8)
plt.plot(x60_clear, y60_clear, linestyle='none', marker='o', 
         label='60 clear', color=colors[4], mfc='w', markersize=8)
plt.plot(x30_clear, y30_clear, linestyle='none', marker='s', 
         label='30 clear', color=colors[5], mfc='w', markersize=8)


#automatically set ticks
xticks = np.arange(0,(xmax+1),(xmax/4))
yticks = np.arange(ymin,(ymax+1),(ymax/4))
#or do xticks by hand if they don't look right
xticks = np.arange(100,800,200)
yticks = np.arange(60,121,20)


#Define tick parameters
plt.minorticks_on()
plt.tick_params(direction='in',which='minor', length=5, 
                bottom=True, top=True, left=True, right=True)
plt.tick_params(direction='in',which='major', length=10, 
                bottom=True, top=True, left=True, right=True)
plt.tick_params(labelbottom=False, labeltop=False, 
                labelright=True, labelleft=False)

plt.xticks(xticks)
plt.yticks(yticks)

#set plot limits
plt.xlim(xmin,xmax)
plt.ylim(ymin,ymax)



plt.legend()


#generate third panel
xtr_subsplot = fig.add_subplot(gs[2:4,2:4])
plt.plot(x90_clear, y90_clear, linestyle='none', marker='^', 
         label='90 clear', color=colors[3], mfc='w', markersize=8)
plt.plot(x60_clear, y60_clear, linestyle='none', marker='o', 
         label='60 clear', color=colors[4], mfc='w', markersize=8)
plt.plot(x30_clear, y30_clear, linestyle='none', marker='s', 
         label='30 clear', color=colors[5], mfc='w', markersize=8)


#automatically set ticks
xticks = np.arange(0,(xmax+1),(xmax/4))
yticks = np.arange(ymin,(ymax+1),(ymax/4))
#or do xticks by hand if they don't look right
xticks = np.arange(100,800,200)
yticks = np.arange(60,121,20)


#Define tick parameters
plt.minorticks_on()
plt.tick_params(direction='in',which='minor', length=5, 
                bottom=True, top=True, left=True, right=True)
plt.tick_params(direction='in',which='major', length=10, 
                bottom=True, top=True, left=True, right=True)
plt.tick_params(labelbottom=True, labeltop=False, 
                labelright=True, labelleft=False)

plt.xticks(xticks)
plt.yticks(yticks)

#set plot limits
plt.xlim(xmin,xmax)
plt.ylim(ymin,ymax)



plt.legend()

#Export figure
plt.savefig('data_for_exercises/plotting/multi_panel_error.png', dpi=300,bbox_inches="tight")
