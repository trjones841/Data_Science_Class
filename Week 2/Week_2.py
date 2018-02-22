
'''
Pandas
http://stackoverflow.com - help

http://planetpython.org

http://dataskeptic.com


















'''

import pandas as pd

pd.Series
animals = ['Tiger', 'Bear', 'Moose']
print(pd.Series(animals))
print('\n')
numbers = [1, 2, 3]
print(pd.Series(numbers))
print('\n')
animals = ['Tiger', 'Bear', None]
print(pd.Series(animals))
print('\n')
numbers = [1, 2, None]
print(pd.Series(numbers))
print('\n')
import numpy as np
print(np.nan == None)
print('\n')
print(np.nan == np.nan)
print('\n')
print(np.isnan(np.nan))
print('\n')
sports = {'Archery': 'Bhutan',
          'Golf': 'Scotland',
          'Sumo': 'Japan',
          'Taekwondo': 'South Korea'}
s = pd.Series(sports)
print(s)
print('\n')

#Querying a Series
sports = {'Archery': 'Bhutan',
          'Golf': 'Scotland',
          'Sumo': 'Japan',
          'Taekwondo': 'South Korea'}
s = pd.Series(sports)
print(s)
print('\n')
print(s.loc['Golf'])
print('\n')
print(s[3])
print('\n')
print(s['Golf'])
print('\n')
sports = {99: 'Bhutan',
          100: 'Scotland',
          101: 'Japan',
          102: 'South Korea'}
print(pd.Series(sports))
print('\n')
s[0] #This won't call s.iloc[0] as one might expect, it generates an error instead
print('\n')
s = pd.Series([100.00, 120.00, 101.00, 3.00])
print(s)
print('\n')
total = 0
for item in s:
    total+=item
print(total)
print('\n')

import numpy as np

total = np.sum(s)
print(total)
print('\n')

#this creates a big series of random numbers
s = pd.Series(np.random.randint(0,1000,10000))
print(s.head())
print('\n')
print(len(s))
print('\n')
#%%timeit -n 100
summary = 0
for item in s:
    summary+=item
print('\n')
#%%timeit -n 100
print(np.sum(s))
print('\n')
s+=2    #adds two to each item in s using broadcasting
print(s.head())
print('\n')
#set_value is deprecated and will be removed in a future release. Please use .at[] or .iat[] accessors instead s.set_value(label, value+2)
#for label, value in s.iteritems():
#    s.set_value(label, value+2)
print(s.head())
print('\n')

#%%timeit -n 10
s = pd.Series(np.random.randint(0,1000,10000))
for label, value in s.iteritems():
    s.loc[label]= value+2
print('\n')

#%%timeit -n 10
s = pd.Series(np.random.randint(0,1000,10000))
s+=2
print('\n')
s = pd.Series([1, 2, 3])
s.loc['Animal'] = 'Bears'
s
print('\n')
original_sports = pd.Series({'Archery': 'Bhutan',
                             'Golf': 'Scotland',
                             'Sumo': 'Japan',
                             'Taekwondo': 'South Korea'})
cricket_loving_countries = pd.Series(['Australia',
                                      'Barbados',
                                      'Pakistan',
                                      'England'], 
                                   index=['Cricket',
                                          'Cricket',
                                          'Cricket',
                                          'Cricket'])
all_countries = original_sports.append(cricket_loving_countries)
print('\n')
original_sports
print('\n')
cricket_loving_countries
print('\n')
all_countries
print('\n')
all_countries.loc['Cricket']
print('\n')
#
#The DataFrame Data Structure
import pandas as pd
purchase_1 = pd.Series({'Name': 'Chris',
                        'Item Purchased': 'Dog Food',
                        'Cost': 22.50})
purchase_2 = pd.Series({'Name': 'Kevyn',
                        'Item Purchased': 'Kitty Litter',
                        'Cost': 2.50})
purchase_3 = pd.Series({'Name': 'Vinod',
                        'Item Purchased': 'Bird Seed',
                        'Cost': 5.00})
df = pd.DataFrame([purchase_1, purchase_2, purchase_3], index=['Store 1', 'Store 1', 'Store 2'])
print(df.head())
print('\n')

print(df.loc['Store 2'])
print('\n')

print(type(df.loc['Store 2']))
print('\n')

print(df.loc['Store 1'])
print('\n')

print(df.loc['Store 1', 'Cost'])
print('\n')

print('transpose = df.T \n', df.T)
print('\n')

print(df.T.loc['Cost'])
print('\n')

print(df['Cost'])
print('\n')

print(df.loc['Store 1']['Cost'])
print('\n')

print(df.loc[:,['Name', 'Cost']])
print('\n')

print(df.drop('Store 1'))
print('\n')

print(df)
print('\n')

copy_df = df.copy()
copy_df = copy_df.drop('Store 1')
print(copy_df)
print('\n')

print(copy_df.drop)
print('\n')

del copy_df['Name']
print(copy_df)
print('\n')

df['Location'] = None
print(df)
print('\n')
#
# Dataframe Indexing and Loading
costs = df['Cost']
print(costs)
print('\n')

# modifies actual data set
#costs+=2
#print(costs)
#print('\n')

# modifies actual data set
#df['Cost'] *= .8
costs*=.8
print('Costs x 80%: ',costs)
print('\n')
print(df)
print('\n')

