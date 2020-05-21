"""Pandas program to display the first 5 rows of the DataFrame. 
( property_data.csv file)."""

import pandas as pd
data=pd.read_csv('property_data.csv')
print("First 5 rows of DataFrame : ")
print(data.head(5))