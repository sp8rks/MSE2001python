import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('data_for_exercises/UFO.csv')

spots = df[['latitude','longitude']]

df = df.drop(df.columns[6],axis=1)
df['latitude'].describe()
df['longitude'].describe()
df['latitude'] = pd.to_numeric(df['latitude'],errors='coerce')
df['duration (seconds)'] = pd.to_numeric(df['duration (seconds)'],errors='coerce')
df['duration (seconds)'].describe()
df = df.sort_values(['duration (seconds)','latitude'])
df = df.sort_values(['shape','duration (seconds)'])

#value_counts()
a=pd.Series(df['duration (seconds)'].to_numpy())
x = df['state'].value_counts()
df['shape'].value_counts().plot.bar()

#groupby 
y = df.groupby(['shape'], as_index=True).mean()
y = df.groupby(['country'], as_index=True).mean()
y = y.reset_index()
plt.semilogx(df['duration (seconds)'],df['latitude'], marker='o', linestyle='None',mfc='None')

#look for correlations
x1 = np.array(pd.to_numeric(df['longitude'],errors='coerce'))
x2 = np.array(pd.to_numeric(df['latitude'],errors='coerce'))
z = np.corrcoef(x1,x2)


#use latitude longitude to get city, country etc
# from geopy.geocoders import Nominatim
# geolocator = Nominatim(user_agent="Your_name")
# location = geolocator.reverse((spots['latitude'][0]+', '+spots['latitude'][1]), timeout=None)
# print("The Garden of Eden is",location.raw['address']['country'])



