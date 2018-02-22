'''


'''
import pandas as pd

df = pd.read_csv(r'/home/tjones/PycharmProjects/Data_Science_Class/Week 2/census.csv')
print(df.head())
print('\n')

df = df.set_index(['STNAME', 'CTYNAME'])
print(df.head())
print('\n')

df = pd.read_csv(r'/home/tjones/PycharmProjects/Data_Science_Class/Week 2/census.csv')
df.head()
print('\n')

df['SUMLEV'].unique()
print('\n')

df=df[df['SUMLEV'] == 50]
df.head()
print('\n')

columns_to_keep = ['STNAME',
                   'CTYNAME',
                   'BIRTHS2010',
                   'BIRTHS2011',
                   'BIRTHS2012',
                   'BIRTHS2013',
                   'BIRTHS2014',
                   'BIRTHS2015',
                   'POPESTIMATE2010',
                   'POPESTIMATE2011',
                   'POPESTIMATE2012',
                   'POPESTIMATE2013',
                   'POPESTIMATE2014',
                   'POPESTIMATE2015']
df = df[columns_to_keep]
df.head()
print('\n')

df = df.set_index(['STNAME', 'CTYNAME'])
df.head()
print('\n')

df.loc['Michigan', 'Washtenaw County']
print('\n')

df.loc[ [('Michigan', 'Washtenaw County'),
         ('Michigan', 'Wayne County')] ]
print('\n')
