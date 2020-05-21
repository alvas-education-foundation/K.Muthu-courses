"""Pandas program to get the DataFrame ( property_data.csv file)."""

import pandas as pd
# Reading a csv file
data=pd.read_csv('property_data.csv')
print("The DataFrame : ")
print(data)