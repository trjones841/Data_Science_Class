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

print(df)
# Your answer here
#df['Location']= df.index

#Prints the info with Store 1 data
print(df.loc['Store 1'])
print('\n')

print(df.columns)
print('\n')

#Moves the index to column 1 as Name
print(df.set_index(['Name']))
print(df.head())
print('\n')

# Renames a column. Better way to just rename one?
df.columns = ['Cost','Purchases','Name']
print(df)
print('\n')

#Sets the Index name (was empty
df.index.name = ['Location']
print(df)
print('\n')

# Set the index to Name (removes old index - Location)
df = df.set_index('Name')
df = df.sort_index()
print(df)
print('\n')

# Creates 2 indices, Cost, Name
df = df.reset_index()
df = df.set_index(['Cost','Name'])
df = df.sort_index()
print(df)
print('\n')

# Rename a column
df = df.reset_index()
df.columns.values[0] = 'Cost'
print(df)
print('\n')

df = df.reset_index()
print(df)