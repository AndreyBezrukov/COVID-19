#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 15:57:46 2020

@author: andrey
"""

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv')

print(df.head())

dates_columns = list(df.columns)[4:]

print('List of countries:\n', list(set(df.loc[:,'Country/Region'].values)))

df[dates_columns].apply(lambda x: x.sum(), axis=0).plot(style='.')
plt.title('Number of confirmed cases, World')
plt.ylabel('Count')
plt.xlabel('Date')
plt.show()

country = 'China'

df[df.loc[:,'Country/Region'] == country][dates_columns].apply(lambda x: x.sum(), axis=0).plot(style='.')
plt.title('Number of confirmed cases, '+ country)
plt.ylabel('Count')
plt.xlabel('Date')
plt.show()

df[df.loc[:,'Country/Region'] != country][dates_columns].apply(lambda x: x.sum(), axis=0).plot(style='.')
plt.title('Number of confirmed cases, World w/o '+ country)
plt.ylabel('Count')
plt.xlabel('Date')
plt.show()
