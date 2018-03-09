#!/usr/bin/python3

import pandas as pd
import numpy as np
#from scipy.stats import ttest_ind

pd.options.display.max_rows = 120  # default was 60
print('max_rows: ', pd.options.display.max_rows)

pd.options.display.max_columns = 80  # default was 20
print('max_columns: ', pd.options.display.max_columns)
pd.set_option('expand_frame_repr', False)  # Don't wrap data frames

# pd.options.mode.chained_assignment = None  # default='warn'

states = {'OH': 'Ohio', 'KY': 'Kentucky', 'AS': 'American Samoa', 'NV': 'Nevada', 'WY': 'Wyoming', 'NA':
    'National', 'AL': 'Alabama', 'MD': 'Maryland', 'AK': 'Alaska', 'UT': 'Utah', 'OR': 'Oregon', 'MT':
    'Montana', 'IL': 'Illinois', 'TN': 'Tennessee', 'DC': 'District of Columbia', 'VT': 'Vermont', 'ID':
    'Idaho', 'AR': 'Arkansas', 'ME': 'Maine', 'WA': 'Washington', 'HI': 'Hawaii', 'WI': 'Wisconsin', 'MI':
    'Michigan', 'IN': 'Indiana', 'NJ': 'New Jersey', 'AZ': 'Arizona', 'GU': 'Guam', 'MS': 'Mississippi', 'PR':
    'Puerto Rico', 'NC': 'North Carolina', 'TX': 'Texas', 'SD': 'South Dakota', 'MP': 'Northern Mariana Islands',
    'IA': 'Iowa', 'MO': 'Missouri', 'CT': 'Connecticut', 'WV': 'West Virginia', 'SC': 'South Carolina', 'LA':
    'Louisiana', 'KS': 'Kansas', 'NY': 'New York', 'NE': 'Nebraska', 'OK': 'Oklahoma', 'FL': 'Florida', 'CA':
    'California', 'CO': 'Colorado', 'PA': 'Pennsylvania', 'DE': 'Delaware', 'NM': 'New Mexico', 'RI':
    'Rhode Island', 'MN': 'Minnesota', 'VI': 'Virgin Islands', 'NH': 'New Hampshire', 'MA': 'Massachusetts',
    'GA': 'Georgia', 'ND': 'North Dakota', 'VA': 'Virginia'}


def convert_gdplev():
    gdplev = pd.read_excel('gdplev.xls', header=[5], sheet_name='Sheet1', skiprows=[6,7], index_col=[0])
    gdplev.drop(gdplev.columns[[2,6]], axis=1, inplace=True)
    gdplev.index.name = 'Year'
    gdplev.columns = ['Current Annual GDP', '2009 Annual GDP', 'YrQtr', 'Current Quarterly GDP', '2009 Quarterly']
    qtr_gdplev = gdplev.loc[:,'YrQtr':'2009 Quarterly']
    qtr_gdplev = qtr_gdplev.set_index('YrQtr')
    annual_gdplev = gdplev.loc[:, 'Current Annual GDP':'2009 Annual GDP']
    annual_gdplev = annual_gdplev.dropna(axis=0, how='all', thresh=None, subset=None, inplace=False)
    return annual_gdplev, qtr_gdplev


def get_list_of_university_towns():
    '''Returns a DataFrame of towns and the states they are in from the
    university_towns.txt list. The format of the DataFrame should be:
    DataFrame( [ ["Michigan", "Ann Arbor"], ["Michigan", "Yipsilanti"] ],
    columns=["State", "RegionName"]  )

    The following cleaning needs to be done:

    1. For "State", removing characters from "[" to the end.
    2. For "RegionName", when applicable, removing every character from " (" to the end.
    3. Depending on how you read the data, you may need to remove newline character '\n'.
    '''
    import csv
    import re

    text_file = open('university_towns.txt','r')
    mycsv = csv.writer(open('university_towns.csv', 'w'))
    lines = text_file.readlines()
    text_file.close()

    for line in lines:
        if 'edit' in line:
            State = line.split('[')
            continue
        if '(' in line:
            City = line.split('(')
            mycsv.writerow([State, City])

    df = pd.read_csv('university_towns.csv')
    df.columns = ['State','Cities']
    df[['State', 'drop']] = pd.DataFrame(df.State.str.split(n=1, expand=True))
    df = df.drop('drop', 1)
    df[['City', 'Universities']] = pd.DataFrame(df.Cities.str.split(n=1, expand=True))
    df = df.drop('Cities', 1)
    #df['E'] = df['B'].map(lambda x: re.sub(r'\W+', '', x))
    
    return df.head(10)

def get_recession_start():
    '''Returns the year and quarter of the recession start time as a
    string value in a format such as 2005q3'''

    return "ANSWER"


def get_recession_end():
    '''Returns the year and quarter of the recession end time as a
    string value in a format such as 2005q3'''

    return "ANSWER"


def get_recession_bottom():
    '''Returns the year and quarter of the recession bottom time as a
    string value in a format such as 2005q3'''

    return "ANSWER"


def convert_housing_data_to_quarters():
    '''Converts the housing data to quarters and returns it as mean
    values in a dataframe. This dataframe should be a dataframe with
    columns for 2000q1 through 2016q3, and should have a multi-index
    in the shape of ["State","RegionName"].

    Note: Quarters are defined in the assignment description, they are
    not arbitrary three month periods.

    The resulting dataframe should have 67 columns, and 10,730 rows.
    '''

    return "ANSWER"


def run_ttest():
    '''First creates new data showing the decline or growth of housing prices
    between the recession start and the recession bottom. Then runs a ttest
    comparing the university town values to the non-university towns values,
    return whether the alternative hypothesis (that the two groups are the same)
    is true or not as well as the p-value of the confidence.

    Return the tuple (different, p, better) where different=True if the t-test is
    True at a p<0.01 (we reject the null hypothesis), or different=False if
    otherwise (we cannot reject the null hypothesis). The variable p should
    be equal to the exact p value returned from scipy.stats.ttest_ind(). The
    value for better should be either "university town" or "non-university town"
    depending on which has a lower mean price ratio (which is equivilent to a
    reduced market loss).'''

    return "ANSWER"

if __name__ == "__main__":
    #annual_gdp, qtr_gdp = convert_gdplev()
    #print(annual_gdp)
    #print('\n')
    #print(qtr_gdp)
    print(get_list_of_university_towns())
