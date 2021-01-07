import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size' : 14})

x_data = np.arange(0,101,10)
y_data = x_data**2
noise = np.random.randint(-10,10,11)
y_data = np.add(y_data,noise)

fig = plt.figure(1, figsize=(5,5))
plt.semilogy(x_data,y_data,marker='o',markersize=10,mfc='white',
         linestyle='--', label='$y=x^2$')
plt.semilogy(x_data,y_data+500,marker='s',markersize=10,mfc='white',
         linestyle='-', label='$y=x^2+500$')

plt.xlabel('x variable')
plt.ylabel('y label')
plt.legend()
plt.show()

# %%

rings = {'elves':3, 'men' : 9,'dwarves':7,'sauron':1}
fig = plt.figure(1, figsize=(5,5))

lists = sorted(rings.items(), key=lambda item : item[1])
x,y = zip(*lists)

#plt.bar(x,y)
plt.barh(x,y)
explode = (0,0.1,0,0)
#plt.pie(y, labels=x, explode=explode)

# %%
x_data = np.arange(0,50,1)
y_data = np.arange(0,50,1)
colors = np.arange(0,50,1)
area = np.random.rand(50)**2*1000
fig = plt.figure(1, figsize=(5,5))
plt.scatter(x_data,y_data,c=colors,s=area,alpha=0.8)

# %%
failure_data = np.random.normal(size=300000)*200

plt.hist(failure_data,bins=50)

# %%

x_data = np.arange(0,2*np.pi+0.1,np.pi/6)
y_data = np.sin(x_data)
y_error = np.linspace(0,2,13)
x_error = np.linspace(0,0.2,13)
fig = plt.figure(1, figsize=(5,5))
plt.errorbar(x_data, y_data, yerr=y_error, xerr=x_error,
             marker='o', linestyle='none',
             mfc='w', capsize=5, markersize=10)
plt.errorbar(x_data, y_data*5, yerr=y_error, xerr=x_error,
             marker='o', linestyle='none',
             mfc='w', capsize=5, markersize=10)
plt.fill_between(x_data,y_data,y_data*5,color='grey')
















