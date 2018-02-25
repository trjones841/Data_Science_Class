'''


'''
import pandas as pd

# !cat olympics.csv - works in Jypitar env
# for Pycharm, have file with location
df = pd.read_csv('olympics.csv')
print(df.head())
print('\n')


df = pd.read_csv('olympics.csv', index_col = 0, skiprows=1)
print(df.head())
print('\n')

print(df.columns)
print('\n')

for col in df.columns:
    if col[:2]=='01':
        df.rename(columns={col:'Gold' + col[4:]}, inplace=True)
    if col[:2]=='02':
        df.rename(columns={col:'Silver' + col[4:]}, inplace=True)
    if col[:2]=='03':
        df.rename(columns={col:'Bronze' + col[4:]}, inplace=True)
    if col[:1]=='№':
        df.rename(columns={col:'#' + col[1:]}, inplace=True)

print(df.head())
print('\n')
#
# Querying a DataFrame
only_gold = df.where(df['gold'] > 0)
only_gold.head()
print('\n')

only_gold['gold'].count()
print('\n')

df['gold'].count()
print('\n')

only_gold = only_gold.dropna()
only_gold.head()
print('\n')

only_gold = df[df['gold'] > 0]
only_gold.head()
print('\n')

len(df[(df['gold'] > 0) | (df['gold.1'] > 0)])
print('\n')

df[(df['gold.1'] > 0) & (df['gold'] == 0)]
print('\n')
#
# Indexing Dataframes
df.head()
print('\n')

df['country'] = df.index
df = df.set_index('gold')
df.head()
print('\n')

df = df.reset_index()
df.head()
print('\n')

df.head()