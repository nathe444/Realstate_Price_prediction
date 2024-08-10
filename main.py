import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


df1 = pd.read_csv('Bengaluru_House_Data.csv')
# print(df1.groupby('area_type')['area_type'].agg('count'))
df2 = df1.drop(['area_type', 'society', 'balcony', 'availability'], axis='columns')

df3 = df2.dropna()
# print(df3.isnull().sum())

df3['bhk'] = df3['size'].apply(lambda x: int(x.split(' ')[0]))


def convertRange(x):
   array = x.split('-')
   if len(array)==2:
      return (float(array[0])+float(array[1]))/2
   try:
      return float(x)
   except:
      return None

df4 = df3.copy()
df4['total-sqft'] = df4['total_sqft'].apply(convertRange)

df5 = df4.copy()


df5['price_per_sqft'] = df5['price'].apply(float) * 100000 / df5['total-sqft']

df5.location = df5['location'].apply(lambda x: x.strip())

location_stats = df5.groupby('location')['location'].agg('count').sort_values(ascending=False)

otherlocation = location_stats[location_stats<=10] 
#This part creates a boolean mask (a Series of True and False values) by applying the condition < 10 to each value in location_stats.

df5['location'] = df5['location'].apply(lambda x:'other' if x  in otherlocation else x)

print(len(df5.location.unique()))


