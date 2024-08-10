import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


df1 = pd.read_csv('Bengaluru_House_Data.csv')
# print(df1.groupby('area_type')['area_type'].agg('count'))
df2 = df1.drop(['area_type', 'society', 'balcony', 'availability'], axis='columns')

df3 = df2.dropna()
# print(df3.isnull().sum())

df3['bhk'] = df3['size'].apply(lambda x: int(x.split(' ')[0]))

# print(df3.total_sqft.unique())


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

print(df4['total-sqft'].unique)


