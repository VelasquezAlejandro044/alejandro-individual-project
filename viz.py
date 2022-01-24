import pandas as pd
import numpy as np


import matplotlib.pyplot as plt
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
# Plot split data 
################################################################


def plot_split(train, test): 
    # It joins and graphs the train and test data sets together  
    plt.plot(train.index, train.weekly_sales)
    plt.plot(test.index, test.weekly_sales)


################################################################
# Visual aids to understand data and seasonality
################################################################

def target_average_sales_by_month(y):
    """
    It plost sales by month
    """
    ax = y.groupby(y.index.month).mean().plot.bar(width=.9, ec='black')
    plt.xticks(rotation=0)
    ax.set(title='Average Sales by Month', xlabel='Month', ylabel='Sales $US')

def target_average_sales_by_week(y):
    """
    It plost sales by week
    """
    ax = y.groupby(y.index.week).mean().plot.bar(width=.9, ec='black')
    plt.xticks(rotation=90)
    ax.set(title='Average Sales by Week', xlabel='Week number', ylabel='$US')

def week_month_quarter_running_average(y):
    """
    Function plots running average for weekly, monthly and quarterly sales
    """

    y.resample('W').mean().plot(alpha=.8, label='Weekly')
    y.resample('M').mean().plot(label='Montly')
    y.resample('3M').mean().plot(label='Quarterly')
    plt.legend()