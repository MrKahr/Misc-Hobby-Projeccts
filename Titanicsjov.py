# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 19:05:17 2021

@author: mdsan
"""

# Numerical analysis, dataframe management and graphical representation

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 


# Import dataset

filepath = "test.csv"
df = pd.read_csv(filepath)

# Inspecting the dataset
# Collect in a function when you have the time!
def data_desc(df):
    print(df.head())
    print(df.tail())
    print(df.columns)
    print(df.size)
    print(df.info())
    print(df.describe())
   
# Options for pandas 
def options(disp_rows = 0, disp_cols = 0):
    print(f'''Maximum number of rows,cols to display {disp_rows},{disp_cols}''')
    pd.set_option('max_rows', disp_rows)
    pd.set_option('max_columns', disp_cols)

# Subsetting in pandas
df_age = df.Age
df_age_child = df[df.Age < 15]
df_age_child_men = df[(df.Age < 15) & (df.Sex == "male")]

# Create a table of observations 
# Count the number of observations in each column 
def count_obs(df, my_list):
    observations = []
    for element in my_list:
        observations.append(df[element].count())
    return observations 


# Create a list of column names 
def row_names(df):
    names = []
    for element in df.columns:
        names.append(element)
    return names


# Create a data frame 
def create_df(df,my_list):
    col_names = ["Variable","Count"]
    var_names = row_names(df)
    var_count = count_obs(df,my_list)
    return pd.Dataframe(var_count)


# Create a histogram 

# Create a bargraph 


s


