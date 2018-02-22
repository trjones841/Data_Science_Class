'''

'''
#
# Missing values

import pandas as pd


df = pd.read_csv(r'/home/tjones/PycharmProjects/Data_Science_Class/Week 2/log.csv')
df
print('\n')

df.fillna
print('\n')

df = df.set_index('time')
df = df.sort_index()
df


df = df.reset_index()
df = df.set_index(['time', 'user'])
df
print('\n')

df = df.fillna(method='ffill')
