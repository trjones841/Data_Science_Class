# Assignment 3

# Question 1 (20%)
# Load the energy data from the file Energy Indicators.xls, which is a list of
# indicators of energy supply and renewable electricity production from the United Nations
# for the year 2013, and should be put into a DataFrame with the variable name of energy.

# Keep in mind that this is an Excel file, and not a comma separated values file.
# Also, make sure to exclude the footer and header information from the datafile.
# The first two columns are unneccessary, so you should get rid of them, and you should
# change the column labels so that the columns are:

# ['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable']

# Convert Energy Supply to gigajoules (there are 1,000,000 gigajoules in a petajoule).
# For all countries which have missing data (e.g. data with "...") make sure this is
# reflected as np.NaN values.

# Rename the following list of countries (for use in later questions):

# "Republic of Korea": "South Korea",
# "United States of America": "United States",
# "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
# "China, Hong Kong Special Administrative Region": "Hong Kong"

# There are also several countries with numbers and/or parenthesis in their name. Be
# sure to remove these,

# e.g.

# 'Bolivia (Plurinational State of)' should be 'Bolivia',

# 'Switzerland17' should be 'Switzerland'.


# Next, load the GDP data from the file world_bank.csv, which is a csv containing
# countries' GDP from 1960 to 2015 from World Bank. Call this DataFrame GDP.

# Make sure to skip the header, and rename the following list of countries:

# "Korea, Rep.": "South Korea",
# "Iran, Islamic Rep.": "Iran",
# "Hong Kong SAR, China": "Hong Kong"

# Finally, load the Sciamgo Journal and Country Rank data for Energy Engineering and Power
# Technology from the file scimagojr-3.xlsx, which ranks countries based on their journal
# contributions in the aforementioned area. Call this DataFrame ScimEn.

# Join the three datasets: GDP, Energy, and ScimEn into a new dataset (using the
# intersection of country names). Use only the last 10 years (2006-2015) of GDP data
# and only the top 15 countries by Scimagojr 'Rank' (Rank 1 through 15).

# The index of this DataFrame should be the name of the country, and the columns should
# be ['Rank', 'Documents', 'Citable documents', 'Citations', 'Self-citations',
# 'Citations per document', 'H index', 'Energy Supply', 'Energy Supply per Capita',
# '% Renewable', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014',
# '2015'].

# This function should return a DataFrame with 20 columns and 15 entries.

#######################################################################################################################
import pandas as pd
import numpy as np

pd.options.display.max_rows = 120  # default was 60
print('max_rows: ', pd.options.display.max_rows)

pd.options.display.max_columns = 40  # default was 20
print('max_columns: ', pd.options.display.max_columns)
# pd.set_option('expand_frame_repr', False)  # Don't wrap data frames

# pd.options.mode.chained_assignment = None  # default='warn'

#######################################################################################################################
print('\n### ASSIGNMENT 3 ###')

def answer_one():
    # ******************************************************************************************************************
    # Energy
    # ******************************************************************************************************************
    Energy = pd.read_excel('Energy Indicators.xls', index_col=None, na_values=['NA'], usecols="C:F", header=[17],
                           skip_footer=38)
    Energy.index.name = 'Country'
    Energy.reset_index(level='Country', inplace=True)
    Energy.index.name = 'Index'
    Energy.columns = ['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable']
    Energy.replace('...', np.nan, inplace=True)  # replace ... with NaN
    Energy['Country'] = Energy['Country'].str.replace('\d+', '')  # remove numbers from entries
    Energy['Country'] = Energy['Country'].str.replace(r"\(.*\)",
                                                      "")  # remove entries with parenthesis and all text in between
    Energy['Country'] = Energy['Country'].str.strip()  # strip whitespace
    Energy.replace(to_replace='Republic of Korea', value='South Korea', inplace=True)
    Energy.replace(to_replace='United States of America', value='United States', inplace=True)
    Energy.replace(to_replace='United Kingdom of Great Britain and Northern Ireland', value='United Kingdom',
                   inplace=True)
    Energy.replace(to_replace='China, Hong Kong Special Administrative Region', value='Hong Kong', inplace=True)
    Energy.loc[:, 'Energy Supply'] *= 1000000  # convert from petajoules to gigajoules

    # print(Energy.head(2))

    # ******************************************************************************************************************
    # GDP
    # ******************************************************************************************************************
    # lambda x: x.upper() in ['2015', '2016', '2017']
    GDP = pd.read_csv('world_bank.csv', header=2)
    GDP.index.name = 'Index'
    GDP.rename(index=str, columns={'Country Name': 'Country'}, inplace=True)
    GDP.replace(to_replace='Korea, Rep.', value='South Korea', inplace=True)
    GDP.replace(to_replace='Iran, Islamic Rep.', value='Iran', inplace=True)
    GDP.replace(to_replace='Hong Kong SAR, China', value='Hong Kong', inplace=True)
    GDP.drop(GDP.columns[62], axis=1, inplace=True)

    # df.loc[df['column_name'] == some_value]
    # print('\n\n',GDP.loc[GDP['Country Name'] == 'Iran'])
    # print('\n\n',GDP.head(10))

    # ******************************************************************************************************************
    # ScimEn
    # ******************************************************************************************************************
    ScimEn = pd.read_excel('scimagojr-3.xlsx', index_col=None, na_values=['NA'], usecols="A:H", header=0)
    ScimEn.index.name = 'Index'
    # print('\n\n',ScimEn.loc[ScimEn['Country'] == 'Iran'])
    # print('\n\n',ScimEn)

    # Intersection
    # idx1 = pd.Index([1, 2, 3, 4])
    # idx2 = pd.Index([3, 4, 5, 6])
    #  idx1.intersection(idx2)

    Energy_GDP_df = pd.merge(Energy, GDP, on='Country')
    Energy_GDP_ScimEn_df = pd.merge(Energy_GDP_df, ScimEn, on='Country')

    columns_names = ['Country']+['Rank', 'Documents', 'Citable documents', 'Citations', 'Self-citations', 'Citations per document',
                     'H index',
                     'Energy Supply', 'Energy Supply per Capita', '% Renewable', '2006', '2007', '2008', '2009', '2010',
                     '2011', '2012',
                     '2013', '2014', '2015']

    Energy_GDP_df = pd.merge(Energy, GDP, on='Country')
    Energy_GDP_ScimEn_df = pd.merge(Energy_GDP_df, ScimEn, on='Country')
    Energy_GDP_ScimEn_df.set_index('Country', inplace=True)
    top15_df = Energy_GDP_ScimEn_df[['Rank', 'Documents', 'Citable documents', 'Citations', 'Self-citations',
                                     'Citations per document', 'H index', 'Energy Supply', 'Energy Supply per Capita',
                                     '% Renewable', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013',
                                     '2014', '2015']]
    top15_df = top15_df.sort_values('Rank',ascending=True)
    #print(top15_df.shape)
    return top15_df.head(15)

# print('answer_one():\n', answer_one())

# Question 2 (6.6%)
# The previous question joined three datasets then reduced this to just the top 15
# entries. When you joined the datasets, but before you reduced this to the top 15
# items, how many entries did you lose?

# This function should return a single number.

# Question 2 (6.6%)
# The previous question joined three datasets then reduced this to just the top 15
# entries. When you joined the datasets, but before you reduced this to the top 15
# items, how many entries did you lose?

# This function should return a single number.

def answer_two():
    Energy = pd.read_excel('Energy Indicators.xls', index_col=None, na_values=['NA'], usecols="C:F", header=[17],
                           skip_footer=38)
    Energy.index.name = 'Country'
    Energy.reset_index(level='Country', inplace=True)
    Energy.index.name = 'Index'
    Energy.columns = ['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable']
    Energy.replace('...', np.nan, inplace=True)  # replace ... with NaN
    Energy['Country'] = Energy['Country'].str.replace('\d+', '')  # remove numbers from entries
    Energy['Country'] = Energy['Country'].str.replace(r"\(.*\)",
                                                      "")  # remove entries with parenthesis and all text in between
    Energy['Country'] = Energy['Country'].str.strip()  # strip whitespace
    Energy.replace(to_replace='Republic of Korea', value='South Korea', inplace=True)
    Energy.replace(to_replace='United States of America', value='United States', inplace=True)
    Energy.replace(to_replace='United Kingdom of Great Britain and Northern Ireland', value='United Kingdom',
                   inplace=True)
    Energy.replace(to_replace='China, Hong Kong Special Administrative Region', value='Hong Kong', inplace=True)
    Energy.loc[:, 'Energy Supply'] *= 1000000  # convert from petajoules to gigajoules
    GDP = pd.read_csv('world_bank.csv', header=2)
    GDP.index.name = 'Index'
    GDP.rename(index=str, columns={'Country Name': 'Country'}, inplace=True)
    GDP.replace(to_replace='Korea, Rep.', value='South Korea', inplace=True)
    GDP.replace(to_replace='Iran, Islamic Rep.', value='Iran', inplace=True)
    GDP.replace(to_replace='Hong Kong SAR, China', value='Hong Kong', inplace=True)
    GDP.drop(GDP.columns[62], axis=1, inplace=True)
    ScimEn = pd.read_excel('scimagojr-3.xlsx', index_col=None, na_values=['NA'], usecols="A:H", header=0)
    ScimEn.index.name = 'Index'
    Energy_GDP_df = pd.merge(Energy, GDP, on='Country')
    Energy_GDP_ScimEn_df = pd.merge(Energy_GDP_df, ScimEn, on='Country')
    columns_names = ['Country'] + ['Rank', 'Documents', 'Citable documents', 'Citations', 'Self-citations',
                                   'Citations per document',
                                   'H index',
                                   'Energy Supply', 'Energy Supply per Capita', '% Renewable', '2006', '2007', '2008',
                                   '2009', '2010',
                                   '2011', '2012',
                                   '2013', '2014', '2015']
    Energy_GDP_df = pd.merge(Energy, GDP, on='Country')
    Energy_GDP_ScimEn_df = pd.merge(Energy_GDP_df, ScimEn, on='Country')
    Energy_GDP_ScimEn_df.set_index('Country', inplace=True)
    top15_df = answer_one()
    print(top15_df.shape)
    print(Energy_GDP_ScimEn_df.shape)
    return (len(Energy_GDP_ScimEn_df)-len(top15_df))

# print('answer_two(): ', answer_two())

# Answer the following questions in the context of only the top 15 countries by
# Scimagojr Rank (aka the DataFrame returned by answer_one())

# Question 3 (6.6%)
# What is the average GDP over the last 10 years for each country? (exclude missing
# values from this calculation.)

# This function should return a Series named avgGDP with 15 countries and their average
# GDP sorted in descending order.


def answer_three():
    Top15 = answer_one()
    Top15['AvgGDP'] = (Top15['2006'] + Top15['2007'] + Top15['2008'] + Top15['2009'] + Top15['2010'] + Top15['2011'] + \
             Top15['2012'] + Top15['2013'] + Top15['2014'] + Top15['2015'])/10
    #print(type(Top15['AvgGDP']))
    return Top15['AvgGDP']

 #print('answer_three(): \n', answer_three())

# Question 4 (6.6%)
# By how much had the GDP changed over the 10 year span for the country with the 6th
# largest average GDP?

# This function should return a single number.


def answer_four():
    Top15 = answer_one()
    return ((Top15.iloc[6]['2015'] - Top15.iloc[6]['2006'])/Top15.iloc[6]['2006'])


#print('answer_four(): \n', answer_four())

# Question 5 (6.6%)
# What is the mean Energy Supply per Capita?

# This function should return a single number.


def answer_five():
    Top15 = answer_one()
    return Top15['Energy Supply per Capita'].mean()


#print('answer_five(): \n', answer_five())

# Question 6 (6.6%)
# What country has the maximum % Renewable and what is the percentage?

# This function should return a tuple with the name of the country and the percentage.


def answer_six():
    Top15 = answer_one()
    return (Top15['% Renewable'].idxmax(), Top15['% Renewable'].max)


print('answer_six(): \n', answer_six())


# Question 7 (6.6%)
# Create a new column that is the ratio of Self-Citations to Total Citations. What is the
# maximum value for this new column, and what country has the highest ratio?

# This function should return a tuple with the name of the country and the ratio.


def answer_seven():
    Top15 = answer_one()
    Top15['% Citations'] = (Top15['Self-citations']/Top15['Citations'])
    return (Top15['% Citations'].idxmax(), Top15['% Citations'].max())


#print('answer_seven(): \n', answer_seven())

# Question 8 (6.6%)
# Create a column that estimates the population using Energy Supply and Energy Supply per
# capita. What is the third most populous country according to this estimate?

# This function should return a single string value.


def answer_eight():
    Top15 = answer_one()
    # print(list(Top15))
    Top15['capita'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
    Top15.sort_values(['capita'])
    populous = Top15.index[Top15['capita'] == Top15['capita'].iloc[3]].tolist()
    return populous.pop()


# print('answer_eight(): \n', answer_eight())


# Question 9 (6.6%)
# Create a column that estimates the number of citable documents per person. What is the
# correlation between the number of citable documents per capita and the energy supply per
# capita? Use the .corr() method, (Pearson's correlation).

# This function should return a single number.

# (Optional: Use the built-in function plot9() to visualize the relationship between
# Energy Supply per Capita vs. Citable docs per Capita)


def answer_nine():
    Top15 = answer_one()
    Top15['Citable docs per Capita'] = Top15['Citations'] / (Top15['Energy Supply'] / Top15['Energy Supply per Capita'])
    return Top15['Citable docs per Capita'].corr(Top15['Energy Supply per Capita'])


# print('answer_nine(): \n', answer_nine())


import matplotlib as plt

def plot9():
    #import matplotlib as plt
    #% matplotlib
    #inline

    Top15 = answer_one()
    Top15['PopEst'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
    Top15['Citable docs per Capita'] = Top15['Citable documents'] / Top15['PopEst']
    Top15.plot(x='Citable docs per Capita', y='Energy Supply per Capita', kind='scatter', xlim=[0, 0.0006])


# plot9() # Be sure to comment out plot9() before submitting the assignment!

# Question 10 (6.6%)
# Create a new column with a 1 if the country's % Renewable value is at or above the median
# for all countries in the top 15, and a 0 if the country's % Renewable value is below the median.

# This function should return a series named HighRenew whose index is the country name
# sorted in ascending order of rank.


def answer_ten():
    Top15 = answer_one()
    print(list(Top15))
    total_median = Top15['% Renewable'].median()
    print(total_median)
    #if Top15['% Renewable'] >= total_median:
    #    Top15['AbvMedian'] = '1'
    #else:
    #    Top15['AbvMedian'] = '0'
    return "ANSWER"


print('answer_ten(): \n', answer_ten())

# Question 11 (6.6%)
# Use the following dictionary to group the Countries by Continent, then create a
# dateframe that displays the sample size (the number of countries in each continent bin),
# and the sum, mean, and std deviation for the estimated population of each country.

ContinentDict  = {'China':'Asia',
'United States': 'North America',
'Japan': 'Asia',
'United Kingdom': 'Europe',
'Russian Federation': 'Europe',
'Canada': 'North America',
'Germany': 'Europe',
'India': 'Asia',
'France': 'Europe',
'South Korea': 'Asia',
'Italy': 'Europe',
'Spain': 'Europe',
'Iran': 'Asia',
'Australia': 'Australia',
'Brazil': 'South America'}

# This function should return a DataFrame with index named Continent ['Asia', 'Australia',
# 'Europe', 'North America', 'South America'] and columns ['size', 'sum', 'mean', 'std']

def answer_eleven():
    Top15 = answer_one()
    idx = pd.MultiIndex.from_product([['Continent'], ['Asia', 'Australia', 'Europe', 'North America', 'South America']])
    cols = ['size', 'sum', 'mean', 'std']
    eleven_df = pd.DataFrame('-', idx, cols)
    eleven_data = pd.DataFrame.from_dict(ContinentDict,orient='index')
    #eleven_data.columns=["Continent"]
    #for item in cols:
    #   eleven_data.columns=[item]
    #    eleven_data[item] = pd.Series('-', index=eleven_data.index)
    stacked = eleven_data.stack()
    print('stacked: \n', stacked)
    #eleven_df.set_index(['Continent'],inplace=True)
    #pd.merge(Energy_GDP_df, ScimEn, on='Country')
    # eleven_df = pd.merge(eleven_df,eleven_data)
    print(eleven_data)
    #for cntry,key in ContinentDict.items():
    #    print(cntry,key)
    #    if eleven_df.index.name == key

    # print('\n')
    return eleven_df


# print('answer_eleven(): \n', answer_eleven())


# Question 12 (6.6%)
# Cut % Renewable into 5 bins. Group Top15 by the Continent, as well as these new % Renewable
# bins. How many countries are in each of these groups?

# This function should return a Series with a MultiIndex of Continent, then the bins for
# % Renewable. Do not include groups with no countries.

def answer_twelve():
    Top15 = answer_one()
    # print(list(Top15))
    return "ANSWER"


# print('answer_twelve(): \n', answer_twelve())


# Question 13 (6.6%)
# Convert the Population Estimate series to a string with thousands separator (using commas).
# Do not round the results.

# e.g. 317615384.61538464 -> 317,615,384.61538464

# This function should return a Series PopEst whose index is the country name and whose
# values are the population estimate string.

def answer_thirteen():
    Top15 = answer_one()
    # print(list(Top15))
    return "ANSWER"


# print('answer_thirteen(): \n', answer_thirteen())


# Optional
# Use the built in function plot_optional() to see an example visualization.

def plot_optional():
    #import matplotlib as plt
    #% matplotlib
    #inline
    Top15 = answer_one()
    ax = Top15.plot(x='Rank', y='% Renewable', kind='scatter',
                    c=['#e41a1c', '#377eb8', '#e41a1c', '#4daf4a', '#4daf4a', '#377eb8', '#4daf4a', '#e41a1c',
                       '#4daf4a', '#e41a1c', '#4daf4a', '#4daf4a', '#e41a1c', '#dede00', '#ff7f00'],
                    xticks=range(1, 16), s=6 * Top15['2014'] / 10 ** 10, alpha=.75, figsize=[16, 6]);


    for i, txt in enumerate(Top15.index):
        ax.annotate(txt, [Top15['Rank'][i], Top15['% Renewable'][i]], ha='center')

    print("This is an example of a visualization that can be created to help understand the data. \
    This is a bubble chart showing % Renewable vs. Rank. The size of the bubble corresponds to the countries' \
    2014 GDP, and the color corresponds to the continent.")

    # plot_optional() # Be sure to comment out plot_optional() before submitting the assignment!