# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 19:05:17 2021

@author: mdsan
"""

# Packages for numerical analysis, dataframe management and graphical representation

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 


# Import dataset

# Create relative filepath
filepath = "test.csv"
df = pd.read_csv(filepath)


# Inspecting the dataset
# Collect in a function when you have the time!
def dataDesc(df):
    print(df.head())
    print(df.tail())
    print(df.columns)
    print(df.size)
    print(df.info())
    print(df.describe())
   

# Set options for pandas 
def options(disp_rows = 0, disp_cols = 0):
    print(f'''Maximum number of rows,cols to display {disp_rows},{disp_cols}''')
    pd.set_option('max_rows', disp_rows)
    pd.set_option('max_columns', disp_cols)


# Subsetting in pandas
df_age = df.Age
df_age_child = df[df.Age < 15]
df_age_child_men = df[(df.Age < 15) & (df.Sex == "male")]

### PANDAS --- Create frequency plot 
## TO DO 
## Create frequency plot using matplotlib 

# Create a list of column names 
def rowNames(df):
    names = []
    for element in df.columns:
        names.append(element)
    return names


# Count the number of observations in each column specified
def countObs(df, my_list):
    observations = []
    for element in my_list:
        observations.append(df[element].count())
    return observations 


# Create a frequency table in dataframe 
def createDf(df):
    col_names = ["Variable","Count"]
    var_names = rowNames(df)
    var_count = countObs(df,var_names)
    my_df = pd.DataFrame(list(zip(var_names,var_count)), columns = col_names)
    print(f'Column names are: {col_names}\nRow names are {var_names}\nCounts are {var_count}')
    return my_df


### numpy and Matplotlib --- Create frequency plot 

# Create a histogram 

# Create a bargraph 



