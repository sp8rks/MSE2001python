import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import pandas as pd
import numpy as np
import matplotlib as mpl
import seaborn as sns

mpl.rcParams['pdf.fonttype'] = 42
mpl.rcParams['font.size']=14

filename = r'data_for_exercises/avrami steel.xlsx'
df = pd.read_excel(filename)
x400 = df['400x'].dropna()
y400 = df['400y'].dropna()
x450 = df['450x'].dropna()
y450 = df['450y'].dropna()
x482 = df['482x'].dropna()
y482 = df['482y'].dropna()
x551 = df['551x'].dropna()
y551 = df['551y'].dropna()



Temp = np.array([400,450,482,551])
Temp = Temp+273
invTemp = 1. / Temp

fig = plt.figure(1, figsize=[6,6])

colors = sns.cubehelix_palette(5, start=2)

def avrami(x,k,n):
    return 1-np.exp(-k*x**n)

popt,pcov = curve_fit(avrami,x400,y400)
k=popt[0]
n=popt[1]
plt.semilogx(x400,y400,marker='o', color=colors[1], markersize=11, mfc='white',label='400')
plt.semilogx(x400,avrami(x400,*popt),marker='None', linestyle='-',color=colors[1], markersize=11, mfc='white',label='fit')

plt.semilogx(x450,y450,marker='s', color=colors[2], markersize=11,mfc='white',label='450')
plt.semilogx(x482,y482,marker='^', color=colors[3], markersize=11,mfc='white',label='482')
plt.semilogx(x551,y551,marker='v', color=colors[4], markersize=11,mfc='white',label='551')


plt.minorticks_on()
plt.tick_params(direction='in',right=True, top=True, left=True, bottom=True)
plt.tick_params(labelbottom=True, labeltop=False, labelright=False, labelleft=True)  
plt.tick_params(direction='in',which='minor', length=5, bottom=True, top=True, left=True, right=True)
plt.tick_params(direction='in',which='major', length=10, bottom=True, top=True, left=True, right=True)
plt.xlim([0.1,1e5])
plt.xlabel('time (s)')
plt.ylabel('fraction transformed') 
plt.legend(fontsize=14)




plt.savefig('data_for_exercises/plotting/avrami.png', dpi=300,bbox_inches="tight")