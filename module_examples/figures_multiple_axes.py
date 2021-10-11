import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib.ticker import MultipleLocator
plt.rcParams['font.size']=14

#read data from excel sheet where each value is stored in a different sheet
path = r"data_for_exercises"
filename = r"multiple_axes.xlsx"
xls = pd.ExcelFile(path + '/' + filename)
sheets = xls.sheet_names

#grab data from excel sheet and store into a dictionary of dataframes for each sheet
df = {}
for sheet in sheets: df[sheet] = pd.read_excel(xls, sheet_name=sheet,header=None)

#grab individual data sets from the dictionary df
x = df['cycle100'].iloc[:,0]
x2 = df['cycle20'].iloc[:, 0]
y1 = df['c_cap_ng'].iloc[:,0]
y2 = df['eff_ng'].iloc[:,0]
y3 = df['ded_ng'].iloc[:,0]
y4 = df['d_cap_ng'].iloc[:,0]
y5 = df['eff_g'].iloc[:,0]
y6 = df['ded_g'].iloc[:,0]
y7 = df['c_cap_g'].iloc[:,0]
y8 = df['d_cap_g'].iloc[:,0]

#grab Ram's colors
seshadri = ['#c3121e', '#0348a1', '#ffb01c', '#027608', '#0193b0', '#9c5300', '#949c01', '#7104b5']
#            0sangre,   1neptune,  2pumpkin,  3clover,   4denim,    5cocoa,    6cumin,    7berry

#create custom function to turn axes invisible
def make_patch_spines_invisible(ax):
    ax.set_frame_on(True)
    ax.patch.set_visible(False)
    for sp in ax.spines.values():
        sp.set_visible(False)

#Create figure with subplots for main figure and for the extra axes
fig, host = plt.subplots(figsize=(5, 5.5))
fig.subplots_adjust(right=0.95)
#twinx() creates another axes sharing the x axis. We do this twice for 
#red and blue extra axes
par1 = host.twinx()
par2 = host.twinx()

# Offset the right spine of par2.  The ticks and label have already been
# placed on the right by twinx above.
par2.spines["right"].set_position(("axes", 1.2))
# Having been created by twinx, par2 has its frame off, so the line of its
# detached spine is invisible.  First, activate the frame but make the patch
# and spines invisible.
make_patch_spines_invisible(par2)
# Second, show the right spine.
par2.spines["right"].set_visible(True)

#plot data paying attention to host vs par1 vs par2
p1, = host.plot(x, y1, color=seshadri[1], marker='o', linestyle='None', mew=1, mfc='w', alpha=.8, markersize=8, label=r'charge 15L/min')
p4, = host.plot(x, y4, color=seshadri[1], marker='o', linestyle='None', mew=1, mfc='gray', alpha=.8, markersize=8, label=r'discharge 15L/min')
p2, = par1.plot(x, y2, color=seshadri[0], marker='P', linestyle='None', mew=1, mfc='w', alpha=.8, markersize=8, label=r'15L/min')
p5, = par1.plot(x2, y5, color=seshadri[0], marker='P', linestyle='None', mew=1, mfc='gray', alpha=.8, markersize=8, label=r'15,10L/min')
p3, = par2.plot(x, y3, color=seshadri[4], marker='D', linestyle='None', mew=1, mfc='w', alpha=.8, markersize=8, label=r'15L/min')
p6, = par2.plot(x2, y6, color=seshadri[4], marker='D', linestyle='None', mew=1, mfc='gray', alpha=.8, markersize=8, label=r'15,10L/min')
p7, = host.plot(x2, y7, color=seshadri[1], marker='s', linestyle='None', mew=1, mfc='w', alpha=.8, markersize=8, label=r'charge 15,10L/min')
p8, = host.plot(x2, y8, color=seshadri[1], marker='s', linestyle='None', mew=1, mfc='gray', alpha=.8, markersize=8, label=r'discharge 15,10L/min')

#set axes limits for host, par1, par2
host.set_xlim(0, 100)
host.set_ylim(0, 1200)
par1.set_ylim(0, 105)
par2.set_ylim(300, 1800)

#set axes labels for host, par1, par2
host.set_xlabel("Cycle")
host.set_ylabel(r'Capacity (mA.h/g)')
par1.set_ylabel(r'Coulombic Efficiency (%)')
par2.set_ylabel(r'Discharge Energy Density (W.h/kg)')

#set axis label colors for host, par1, par2
host.yaxis.label.set_color(seshadri[1])
par1.yaxis.label.set_color(seshadri[0])
par2.yaxis.label.set_color(seshadri[4])

#define tick parameters for host, par1, par2
tkw = dict(size=6, width=1.5)
minorLocatory = MultipleLocator(100)
minorLocatorx = MultipleLocator(10)
host.yaxis.set_minor_locator(minorLocatory)
host.xaxis.set_minor_locator(minorLocatorx)

minorLocatory = MultipleLocator(10)
par1.yaxis.set_minor_locator(minorLocatory)

minorLocatory = MultipleLocator(100)
par2.yaxis.set_minor_locator(minorLocatory)

#set colors for host, par1, par2 axes
host.tick_params(axis='y', colors=seshadri[1], **tkw)
par1.tick_params(axis='y', colors=seshadri[0], **tkw)
par2.tick_params(axis='y', colors=seshadri[4], **tkw)
host.tick_params(direction='in', **tkw)
par1.spines["right"].set_edgecolor(p2.get_color())
par2.spines["right"].set_edgecolor(p3.get_color())

lines = [p1, p4, p2, p5, p3, p6, p7, p8]

host.legend(lines, [l.get_label() for l in lines],fontsize=12, frameon=False,loc=1, bbox_to_anchor=(1.02,0.9))

plt.savefig('data_for_exercises/plotting/multiple_axes.eps', dpi=300, bbox_inches='tight')
plt.savefig('data_for_exercises/plotting/multiple_axes.png', dpi=300, bbox_inches='tight')

plt.show()