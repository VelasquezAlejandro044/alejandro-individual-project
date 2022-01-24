# imports
import numpy as np
import pandas as pd

from datetime import datetime
from sklearn.metrics import mean_squared_error
from math import sqrt

import matplotlib.pyplot as plt
import seaborn as sns
from pandas.plotting import register_matplotlib_converters

import statsmodels.api as sm
from statsmodels.tsa.api import Holt

from viz import plot_samples

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
# The following functions will help evaluate each of the forecasting methods.
################################################################
def plot_samples(target_var):
    '''
    This function will plot the train and test values for a single variable across all dates. 
    '''
    plt.figure(figsize=(12,4))
    plt.plot(train[target_var])
    plt.plot(test[target_var])
    plt.title(target_var)
    
    # evaluation function to compute rmse
def evaluate(train, yhat_df, target_var):
    """
    Function will compute the Mean Squared Error and the Rood Mean Squared Error to evaluate.
    """
    rmse = round(sqrt(mean_squared_error(train[target_var], yhat_df[target_var])), 0)
    return rmse

# plot and evaluate 
def plot_and_eval(target_var):
    """
    Function will plot train and test values with the predicted
    values to compare performance.
    """
    plot_samples(target_var)
    plt.plot(yhat_df[target_var])
    plt.title(target_var)
    rmse = evaluate(target_var)
    print(target_var, '--RMSE: {:.0f}'.format(rmse))
    plt.show()
    
    # Function to store rmse for comparison purposes
def append_eval_df(model_type, target_var):
    """
    Append evaluation metrics for each model type, target variable, and metric 
    type, along with the metric value, into our eval_df data frame object. Which 
    we will create an empty eval_df data frame object to start.
    """
    rmse = evaluate(target_var)
    d = {'model_type': [model_type], 'target_var': [target_var], 'rmse': [rmse]}
    d = pd.DataFrame(d)
    return eval_df.append(d, ignore_index = True)

# Create an empty data frame where all the results of the models will go  
def evaluate_data_frame():
    eval_df = pd.DataFrame(columns=['model_type', 'target_var', 'rmse'])
    return eval_df
################################################################
# Modeling aids
################################################################
def make_predictions(weekly_sales):
    yhat_df = pd.DataFrame({'weekly_sales': [weekly_sales]}, index = train.index)
    return yhat_df



def best_model(eval_df):
    """
    Functions calculates lowest RMSE
    """
    # get the min rmse for each variable
    min_rmse_weekly_sales = eval_df.groupby('target_var')['rmse'].min()[0]
    
    # filter only the rows that match those rmse to find out 
    # which models are best thus far
    return eval_df[((eval_df.rmse == min_rmse_weekly_sales))]

