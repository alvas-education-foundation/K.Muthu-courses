"""Show the fields of CSV files and sorted by the field ST_NAME"""

import pandas as pd
data=pd.read_csv('property_data.csv')
print("Fields of the CSV file :")
print(data.columns)
s=data.sort_values('ST_NAME')
print("Data sorted based on <ST_NAME> field")
print(s)