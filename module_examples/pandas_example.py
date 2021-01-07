import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas_profiling import ProfileReport

df = pd.read_csv('data_for_exercises/UFO.csv')

#df = df.drop(df.columns[6],axis=1)

df = df.drop('duration (hours/min)',axis=1)

df['longitude'].describe()
df['latitude'].describe()
df['duration (seconds)'].describe()
# profile = ProfileReport(df.copy(), title='Pandas Profiling Report of UFO dataset', html={'style':{'full_width':True}})
# #profile.to_widgets()
# #widgets doesn't work in spyder, do html instead
# profile.to_file('profile_report.html')

cols = list(df.columns.values)
cols2 = ['datetime', 'city', 'state', 'country', 'latitude', 'longitude',
 'shape', 'duration (seconds)', 'comments', 'date posted']

df=df[cols2]

df['latitude'] = pd.to_numeric(df['latitude'],errors='coerce')
df['duration (seconds)'] = pd.to_numeric(df['duration (seconds)'],errors='coerce')

df = df.sort_values(['duration (seconds)', 'latitude'])
df = df.sort_values(['shape', 'latitude'])


df2 = df.copy()
bool_latitude = df2['latitude'] > 42
bool_duration = df2['duration (seconds)'] > 10000
df2 = df2.drop(df2.loc[bool_latitude].index, axis=0)
df2 = df2.drop(df2.loc[bool_duration].index, axis=0)
print(f'Cleaned DataFrame shape: {df2.shape}')

#df2 = df2.loc[df2['latitude']>42]

#value_counts
x = df['shape'].value_counts()
#df['shape'].value_counts().plot.bar()

#groupby
y=df.groupby(['shape']).mean()

#plotting
plt.plot(df['longitude'],df['latitude'],linestyle='None', marker='o', markersize=5)


utah_df = df.loc[df['state']=='ut']

for i,lat,long in zip(df.index, df['latitude'],df['longitude']):
    if (lat >37 and lat <41) and (long >-114 and long <-109):
        df.at[i,'Utah'] = True
    elif (lat >41 and lat <42) and (long >-114 and long <-111):
        df.at[i,'Utah'] = True
    else:
        df.at[i,'Utah'] =False

df3 = df.copy()
df3= df3.drop(df3.loc[df3['Utah']==False].index,axis=0)


df.loc[df['comments'].str.contains('UFO',na=False),['comments','latitude']]=['XXXX REDACTED','POSITION HIDDEN']



#use latitude longitude to get city, country etc
# from geopy.geocoders import Nominatim
# geolocator = Nominatim(user_agent="Your_name")
# location = geolocator.reverse((spots['latitude'][0]+', '+spots['latitude'][1]), timeout=None)
# print("The Garden of Eden is",location.raw['address']['country'])







