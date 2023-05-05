# -*- coding: utf-8 -*-
"""
Created on Fri May  5 22:30:57 2023

@author: saad4
"""
import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 

df = pd.read_csv('Cleaned_Internet_Users.csv')

# choose relevant columns 
df.columns

df_model = df[['Year','No of Internet Users','Internet Users(%)','Cellular Subscription']]
# get dummy data 
df_dum = pd.get_dummies(df_model)

# train test split 
from sklearn.model_selection import train_test_split

X = df_dum.drop('Year', axis =1)
y = df_dum['Year'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# multiple linear regression 
import statsmodels.api as sm

X_sm = X = sm.add_constant(X)
model = sm.OLS(y,X_sm)
model.fit().summary()

from sklearn.linear_model import LinearRegression, Lasso
from sklearn.model_selection import cross_val_score

lm = LinearRegression()
lm.fit(X_train, y_train)

np.mean(cross_val_score(lm,X_train,y_train, scoring = 'neg_mean_absolute_error', cv= 3))