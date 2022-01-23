import pandas as pd
import numpy as np
import os
from env import host, user, password

# imports
import numpy as np
import pandas as pd

from datetime import datetime
from sklearn.metrics import mean_squared_error
from math import sqrt

import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
from pandas.plotting import register_matplotlib_converters

import statsmodels.api as sm
from statsmodels.tsa.api import Holt

# Ignore warnings
import warnings
warnings.filterwarnings("ignore")

# supress scientific notation
# np.set_printoptions(suppress=True)
plt.rcParams["axes.formatter.limits"] = (-5, 12)
# pd.options.display.float_format = '{:.2f}'.format

# plt.style.use('seaborn-whitegrid')
plt.rc('figure', figsize=(13, 7))
plt.rc('font', size=16)
plt.style.use('fivethirtyeight')


################################################################
# Acquire
################################################################


def get_walmart_data():
    if os.path.isfile('Walmart.csv') == False:
        print("Data is not cached. Acquiring new power data.")
        df = new_power_data()
    else:
        print("Data is cached. Reading data from .csv file.")
        df = pd.read_csv('Walmart.csv')
    print("Acquisition complete")
    return df


def new_walmart_data():
    df = pd.read_csv("Walmart.csv")
    
    # Chanege CPI for Consumer Price Index
    df.rename(columns={'CPI':'Consumer_Price_Index'}, inplace=True)
    
    # Turn the name of the columns to lower case characters
    df.columns= df.columns.str.lower()

    # Convert our date column from object type to DateTime type and trains kernel to know proper order of date 
    df.date = pd.to_datetime(df.date, format='%d-%m-%Y')  

    # Set the date as index
    df = df.set_index('date', drop=True).sort_index()
    
    return df


