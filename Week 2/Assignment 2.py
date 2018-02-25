import pandas as pd


pd.options.display.max_rows = 60 # default was 60
print('max_rows: ', pd.options.display.max_rows)

pd.options.display.max_columns = 20 # default was 20
print('max_columns: ', pd.options.display.max_columns)
pd.set_option('expand_frame_repr', False) # Don't wrap data frames

# pd.options.mode.chained_assignment = None  # default='warn'

#####################PART 1 ###########################################################################################
print('\n### PART 1 ###')
df = pd.read_csv('olympics.csv', index_col=0, skiprows=1)

for col in df.columns:
    if col[:2]=='01':
        df.rename(columns={col:'Gold'+col[4:]}, inplace=True)
    if col[:2]=='02':
        df.rename(columns={col:'Silver'+col[4:]}, inplace=True)
    if col[:2]=='03':
        df.rename(columns={col:'Bronze'+col[4:]}, inplace=True)
    if col[:1]=='№':
        df.rename(columns={col:'#'+col[1:]}, inplace=True)

names_ids = df.index.str.split('\s\(') # split the index by '('

df.index = names_ids.str[0] # the [0] element is the country name (new index)
df['ID'] = names_ids.str[1].str[:3] # the [1] element is the abbreviation or ID (take first 3 characters from that)

df = df.drop('Totals')
#print(df.head(10))


#Question 1: Which country has won the most gold medals in summer games?
#This function should return a single string value.


def answer_one():
    return df.gold[df.gold == df['gold'].max()].index[0]

print('\nQues1: Country with the most gold medals in the Summer Games:',answer_one())


# Question 2 - Which country had the biggest difference between their summer and winter gold medal counts?
# This function should return a single string value.


def answer_two():
    df['Max_Diff'] = pd.Series(abs(df['gold'] - df['gold.1']))
    return df.sort_values(by='Max_Diff',ascending=False).index[0]

print('\nQues2: Country with biggest gold medal difference between summer & winter games is: ',answer_two())


# Question 3 - Which country has the biggest difference between their summer gold medal counts
# and winter gold medal counts relative to their total gold medal count?

# (Summer Gold−Winter Gold)/Total Gold

# Only include countries that have won at least 1 gold in both summer and winter.
# This function should return a single string value.


def answer_three():
    summer_and_winter_gold = df[(df['gold'] > 0) & (df['gold.1'] > 0)]
    answer3 = (abs(summer_and_winter_gold['gold'] - summer_and_winter_gold['gold.1'])/(summer_and_winter_gold['gold'] + summer_and_winter_gold['gold.1']))
    return answer3.sort_values(ascending=False).index[0]

print('\nQues3: Country that has the biggest difference between their summer & winter gold medal counts: ', answer_three())

# and winter gold medal counts relative to their total gold medal count')

# Question 4 = Write a function that creates a Series called "Points" which is a weighted value where each
# gold medal (Gold.2) counts for 3 points, silver medals (Silver.2) for 2 points, and bronze medals (Bronze.2)
# for 1 point. The function should return only the column (a Series object) which you created, with the country
# names as indices.

# This function should return a Series named Points of length 146


def answer_four():
    df['Points'] = df['gold.2'].multiply(3) + df['silver.2'].multiply(2) + df['bronze.2'].multiply(1)
    return df['Points'].sort_values(ascending=False)

A4 = answer_four()
print('\nQues4: Create series called Points that sums medal totals with gold*3, silver*2 and bronze*1: \n', A4.head())

#####################PART 1 ###########################################################################################
print('\n### PART 2 ###')
# For the next set of questions, we will be using census data from the United States Census Bureau. Counties are 
# political and geographic subdivisions of states in the United States. This dataset contains population data for 
# counties and states in the US from 2010 to 2015. See this document for a description of the variable names.

#The census dataset (census.csv) should be loaded as census_df. Answer questions using this as appropriate.

census_df = pd.read_csv('census.csv', index_col=0, skiprows=0)
#print('Columns: ', list(census_df))
#print('\n',census_df.head(1))

# Question 5
# Which state has the most counties in it? (hint: consider the sumlevel key carefully! You'll need this for future questions too...)
# This function should return a single string value.

def answer_five():
    state_df = census_df[census_df['COUNTY'] != 0]
    return state_df.groupby('STNAME')['COUNTY'].count().sort_values(ascending=False).index[0]

print('\nQues5: State with the most counties is: ',answer_five())

# Question 6
# Only looking at the three most populous counties for each state, what are the three most populous states
#  (in order of highest population to lowest population)? Use CENSUS2010POP.
# This function should return a list of string values.

def answer_six():
    #remove county 0 (is just totals)
    state_df = census_df[census_df['COUNTY'] != 0]
    #sort CENSUS2010POP for each state, then sum first 3 & return as list
    return state_df.groupby('STNAME')['CENSUS2010POP'].nlargest(3).groupby('STNAME').sum().nlargest(3).index.values.tolist()

print('\nQues6: The three most populous states with the three most populous counties is: ',answer_six())

# Question 7
# Which county has had the largest absolute change in population within the period 2010-2015? (Hint: population values
# are stored in columns POPESTIMATE2010 through POPESTIMATE2015, you need to consider all six columns.)
# e.g. If County Population in the 5 year period is 100, 120, 80, 105, 100, 130, then its largest change in the period
# would be |130-80| = 50.
# This function should return a single string value.


def answer_seven():
    state_df = census_df[census_df['COUNTY'] != 0]
    max_pop_per_cty_per_yr = state_df[['CTYNAME','STNAME', 'POPESTIMATE2010', 'POPESTIMATE2011', 'POPESTIMATE2012',
                                       'POPESTIMATE2013', 'POPESTIMATE2014', 'POPESTIMATE2015']]
    max_pop_per_cty_per_yr.set_index(['CTYNAME','STNAME'], inplace=True) # Multiple states with same county name
    DIFF = max_pop_per_cty_per_yr.T.max() - max_pop_per_cty_per_yr.T.min().sort_values(ascending=False)
    result = DIFF.sort_values(ascending=False).index[0]
    return result[0]

print('\nQues7: County with the largest absolute change in population within the period 2010-2015 is: ',answer_seven())

# Question 8
# In this datafile, the United States is broken up into four regions using the "REGION" column.
# Create a query that finds the counties that belong to regions 1 or 2, whose name starts with 'Washington', and whose
# POPESTIMATE2015 was greater than their POPESTIMATE 2014.
# This function should return a 5x2 DataFrame with the columns = ['STNAME', 'CTYNAME'] and the same index ID as the
# census_df (sorted ascending by index).


def answer_eight():
    state_df = census_df[census_df['COUNTY'] != 0]
    region_df = state_df[['REGION', 'CTYNAME', 'STNAME', 'POPESTIMATE2014', 'POPESTIMATE2015']]
    region_df = region_df.loc[((region_df['REGION'] == 1) | (region_df['REGION'] == 2)) &
                             (region_df['CTYNAME'].str.contains('Washington')) &
                              (region_df['POPESTIMATE2015'] > region_df['POPESTIMATE2014'])]
    return region_df.ix[:, ['CTYNAME', 'STNAME']]


A8 = answer_eight()
# print('census_df.index.name: ', census_df.index.name)
# print('index_name: ', A8.index.name)
# print('\ntype: ', type(A8))
print('\nQues8: List of counties that belong to regions 1 or 2, whose name starts with \'Washington\', and '
      'whose POPESTIMATE2015 was greater than their POPESTIMATE 2014\n', A8)