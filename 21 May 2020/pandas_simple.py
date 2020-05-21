"""Pandas program to create the mean,standard deviation, maximum and 
minimum of the data of a given Series.[5, 10, 6, 8, 10]
"""

import pandas as pd
data=pd.Series([5, 10, 6, 8, 10])
print("Original Series : ")
print(data)
print("Mean of data in series : ")
print(data.mean())
print("Standard Deviation of data in series : ")
print(data.std())
print("Max. value of data in series : ")
print(data.max())
print("Min. value of data in series : ")
print(data.min())