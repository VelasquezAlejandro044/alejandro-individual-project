import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import os

################################################################
# Acquire
################################################################


def get_walmart_data():
    # find data locally
    if os.path.isfile('Walmart.csv') == False:
        print("Data is not cached. Acquiring new power data.")
        df = new_power_data()
    else:
        print("Data is cached. Reading data from .csv file.")
        df = pd.read_csv('Walmart.csv')
    print("Acquisition complete")
    return df

################################################################
# Prepare
################################################################


def new_walmart_data(df):
    
    # Chanege CPI for Consumer Price Index
    df.rename(columns={'CPI':'Consumer_Price_Index'}, inplace=True)
    
    # Turn the name of the columns to lower case characters
    df.columns= df.columns.str.lower()

# Convert our date column from object type to DateTime type and trains kernel to know proper order of date 
    df.date = pd.to_datetime(df.date, format='%d-%m-%Y')  

    # Set the date as index
    df = df.set_index('date', drop=True).sort_index()
    
    return df

################################################################
# Split into train and test
################################################################

def split_walmart_data(df):
    # Use percentage methodes to split
    train_size = .60
    n = df.shape[0]
    test_start_index = round(train_size * n)
    
    train = df[:test_start_index] # everything up (not including) to the test_start_index
    test = df[test_start_index:] # everything from the test_start_index to the end
    
    # eliminate all variables from train and test exept target 
    train = pd.DataFrame(train['weekly_sales'])
    test = pd.DataFrame(test['weekly_sales'])
    
    return train, test



    
