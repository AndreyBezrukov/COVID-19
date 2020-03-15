#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 15:57:46 2020

@author: andrey
"""
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.optimize import curve_fit
from sklearn.metrics import r2_score

df = pd.read_csv('csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv')

print(df.head())

dates_columns = list(df.columns)[4:]

def exponent(t,  k, t0):
    return np.exp(k * (t-t0))

xdata = [(datetime.strptime(i, '%m/%d/%y')-datetime.strptime(dates_columns[0], '%m/%d/%y')).days for i in dates_columns] 
ydata = df[df.loc[:,'Country/Region'] != 'China'][dates_columns].apply(lambda x: x.sum(), axis=0).values

popt, pcov = curve_fit(exponent, xdata, ydata)

print('Exponential fit:')
print('k:', popt[0], ' t0: ', popt[1])
print('R2: ',r2_score( ydata, exponent(xdata, popt[0], popt[1])))

xdata_datetime = [datetime.strptime(i, '%m/%d/%y') for i in dates_columns]

day_first = 0
day_last = 100

plt.plot(xdata_datetime[day_first:day_last], exponent(xdata, popt[0], popt[1])[day_first:day_last])
plt.scatter(xdata_datetime[day_first:day_last],ydata[day_first:day_last])
plt.title('Number of confirmed cases, World w/o China')
plt.ylabel('Count')
plt.xlabel('Date')
plt.xticks(rotation=90) 
plt.show()


