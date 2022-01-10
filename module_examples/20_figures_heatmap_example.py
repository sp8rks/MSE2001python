import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import matplotlib.gridspec as gridspec
import matplotlib.colors as colors


plt.rcParams['font.size']=14

#grab data
filename = r'data_for_exercises/heatmap.csv'
df = pd.read_csv(filename)

#grab data only from 504 to 4066 so we have Q=2.25 to 4
x1= df.loc[504:4066,'Q'].dropna().to_numpy()
y1 = df.loc[504:4066,'y1'].dropna().to_numpy()
y2 = df.loc[504:4066,'y2'].dropna().to_numpy()
y3 = df.loc[504:4066,'y3'].dropna().to_numpy()
y4 = df.loc[504:4066,'y4'].dropna().to_numpy()
y5 = df.loc[504:4066,'y5'].dropna().to_numpy()
y6 = df.loc[504:4066,'y6'].dropna().to_numpy()
y7 = df.loc[504:4066,'y7'].dropna().to_numpy()
y8 = df.loc[504:4066,'y8'].dropna().to_numpy()
y9 = df.loc[504:4066,'y9'].dropna().to_numpy()
y10 = df.loc[504:4066,'y10'].dropna().to_numpy()
y11 = df.loc[504:4066,'y11'].dropna().to_numpy()
y12 = df.loc[504:4066,'y12'].dropna().to_numpy()
y13 = df.loc[504:4066,'y13'].dropna().to_numpy()
y14 = df.loc[504:4066,'y14'].dropna().to_numpy()
y15 = df.loc[504:4066,'y15'].dropna().to_numpy()
y16 = df.loc[504:4066,'y16'].dropna().to_numpy()
y17 = df.loc[504:4066,'y17'].dropna().to_numpy()
y18 = df.loc[504:4066,'y18'].dropna().to_numpy()
y19 = df.loc[504:4066,'y19'].dropna().to_numpy()
y20 = df.loc[504:4066,'y20'].dropna().to_numpy()
y21 = df.loc[504:4066,'y21'].dropna().to_numpy()

#Create dataframe with 3 columns representing Q, P, and Intensity
#repeat the Q data 21 times in a row
Q=[]
for x in range(21):
    Q = np.append(Q,x1)

#create a list of pressures
Pressure_list = [13.05904722,14.35172223,15.17500971,
                  15.67921839,16.63392168,18.11248028,
                  19.44567268,21.13192835,23.231572,
                  24.9022654,27.52584627,30.25623505,
                  32.35560777,33.63590673,35.89360568,
                  38.28325398,39.57449986,41.96951715,
                  42.12192297,43.51712975,47.27314848]
#Store pressure value 3563 times in a row then loop that 
#for all pressures in list (21)
New_Pressure=[]
for p in Pressure_list:
    Pressure = np.full(3563,p)
    New_Pressure = np.append(New_Pressure,Pressure)
Pressure=New_Pressure

#Create list of all 21 intensities
args = (y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14,y15,y16,y17,y18,y19,y20,y21)
Intensity = np.concatenate(args)
#scale it so we can see it better in heatmap
#Intensity = np.log(Intensity)
Intensity = Intensity**(1/100000)

#here we tell the map which ones we want for x, y, and heat
results = np.transpose(np.vstack([Q,Pressure,Intensity]))
dataset = pd.DataFrame({'Q': Q, 'Pressure (GPa)': Pressure, 'Intensity':Intensity})
dataset = dataset.reset_index().pivot_table(index='Q',columns='Pressure (GPa)',values='Intensity')


# #make figure, define plot
#fig, ax = plt.subplots(figsize=(5,5))

# ax = sns.heatmap(dataset, yticklabels=[2.5,3,3.5,4],xticklabels=[13.06,21.13,33.63,43.51],cbar=False)
# ax.set_yticks([509,1524,2544,3562])
# ax.set_xticks([0,7,13,20])
# ax.set_ylabel('')

# plt.show()

#fig, host = plt.subplots(figsize=(5, 5.5))
fig = plt.figure(1, figsize=(5, 5))
gs = gridspec.GridSpec(4,6)
gs.update(wspace=0.1, hspace=0.25)

#Generate left wing panel
#remember, the grid spec is rows, then columns
xtr_subsplot = fig.add_subplot(gs[0:4,0:1])


#try to match colors
def truncate_colormap(cmap, minval=0.0, maxval=1.0, n=100):
    new_cmap = colors.LinearSegmentedColormap.from_list(
        'trunc({n},{a:.2f},{b:.2f})'.format(n=cmap.name, a=minval, b=maxval),
        cmap(np.linspace(minval, maxval, n)))
    return new_cmap

cmap = plt.get_cmap('rocket')
new_cmap = truncate_colormap(cmap, 0.1, 0.55)

plt.scatter(y1,x1,s=1,c=y1,cmap=new_cmap)
plt.xlabel('')
plt.xticks([])
plt.ylabel('$Q=2\pi/d\,(\AA^{-1})$')
plt.text(33.5,3.9,'P=13.06 GPa',rotation=90)

#get the limits 
xmin=np.min(y1)
xmax=np.max(y1)
plt.xlim(xmax,xmin)
plt.ylim(4,2.25)

#ticks
yticks = np.arange(2.5,4.1,0.5)
plt.minorticks_on()
plt.tick_params(direction='in',which='minor', length=4, 
                bottom=True, top=True, left=True, right=True)
plt.tick_params(direction='in',which='major', length=6, 
                bottom=True, top=True, left=True, right=True)
plt.yticks(yticks)


#Generate right wing panel
#remember, the grid spec is rows, then columns
xtr_subsplot = fig.add_subplot(gs[0:4,5:6])

plt.scatter(y21,x1,s=0.5,c=y21,cmap=new_cmap)
#plt.plot(y21,x1,color='k')
plt.xlabel('')
plt.ylabel('')

plt.xticks([])
xmin=np.min(y21)
xmax=np.max(y21)
plt.xlim(xmin,xmax)
plt.ylim(4,2.25)

#ticks
yticks = np.arange(2.5,4.1,0.5)
plt.minorticks_on()
plt.tick_params(direction='in',which='minor', length=4, 
                bottom=True, top=True, left=True, right=True)
plt.tick_params(direction='in',which='major', length=6, 
                bottom=True, top=True, left=True, right=True)
plt.yticks(yticks)
xtr_subsplot.yaxis.set_label_position("right")
xtr_subsplot.tick_params(labeltop=False, labelright=True)
xtr_subsplot.set_yticklabels([])

plt.text(36,3,'P=43.51 GPa',rotation=90)


#Generate middle heatmap panel
#remember, the grid spec is rows, then columns
xtr_subsplot = fig.add_subplot(gs[0:4,1:5])

#ax = sns.heatmap(dataset, yticklabels=[2.5,3,3.5,4],xticklabels=[13.06,21.13,33.63,43.51],cbar=False)
#ax.set_yticks([509,1524,2544,3562])
fig = sns.heatmap(dataset, yticklabels=False,xticklabels=[13.06,21.13,33.63,43.51],cbar=False)
#these are just approx. we still need to fix these
fig.set_xticks([0,7,13,20])
fig.set_ylabel('')



plt.savefig('data_for_exercises/plotting/heatmap.png', dpi=300, bbox_inches='tight')

plt.show()


#now let's plot the 2D plots as wings on the side



# # %%
# #try it with imshow()

# import matplotlib.pyplot as plt
# import numpy as np


# def heatmap2d(arr: np.ndarray):
#     plt.imshow(arr, cmap='viridis')
#     plt.colorbar()
#     plt.show()

# #Convert our dataframe to a numpy array
# df= df.loc[504:4066,:]
# df = df.set_index('Q')
# test2=df.to_numpy()

# #create 340 copies of each row then append them all together
# #we do this because there are several thousand Q data points,
# #but only 21 pressures. We need to plot each pressure ~200 times
# #so you can see them compared to Q
# test3=[]
# for column in df.columns:
#     test_col = df.loc[:,column].transpose()
#     for i in range(200):
#         test3.append(test_col) 

# heatmap2d(test3)

