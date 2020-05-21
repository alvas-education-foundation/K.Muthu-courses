"""Pandas program to get the details of the 5 th row of the DataFrame 
( property_data.csv file).
"""

#Note:The index starts from 0
import pandas as pd
data=pd.read_csv('property_data.csv')
s=data.iloc[4]
print("Details of 4th row : ")
print(s)