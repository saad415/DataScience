# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a data_cleaning script file.
"""

import pandas as pd

df = pd.read_csv('Internet_Usres.csv')

print("Column datatypes: ")
print(df.dtypes)

#df['Entity'].nunique()

#print(df['Entity'].value_counts())

#print('Before ',  len(df[df['Broadband Subscription'] == 0]))

#df = df[(df['Cellular Subscription'] != 0) & (df['Internet Users(%)'] != 0)]

df.drop(df[df['Internet Users(%)'] < 1].index, inplace=True)

df.describe()

#df = df[(df.Year == 2012) | (df.Year == 2013) ]

#print(df['Entity'].nunique())

df['Cellular Subscription'] = df['Cellular Subscription'].apply(lambda x:round(x,2))

df['Internet Users(%)'] = df['Internet Users(%)'].apply(lambda x:round(x,2))

df['Broadband Subscription'] = df['Broadband Subscription'].apply(lambda x:round(x,2))

df.sort_values(['Entity', 'Year'], ascending=[True, True], inplace=True)

df_out = df.drop(['Unnamed: 0'], axis =1 )

df_out.to_csv('Cleaned_Internet_Users.csv', index=False)

