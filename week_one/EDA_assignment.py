# import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the csv file
data = pd.read_csv(r'C:\Users\user\OneDrive\Desktop\projects\data camp\week_one\IT Salary Survey EU  2020.csv')

df.head()
list(df.columns)  # list column names
df.shape

# remove duplicate and blank rows
df.drop_duplicates(inplace=True)    
df.dropna(inplace=True) #remove blank rows


# count number of rows whilist filtering according to similar data in cell
df.groupby('Gender').count()  
df.groupby('Employment status').count() 
df.groupby('Have you lost your job due to the coronavirus outbreak?').count()   
df.filter(['Have you lost your job due to the coronavirus outbreak?']).groupby(['Employment status']).count()
