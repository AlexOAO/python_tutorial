#
# Template for Python program
#

import pandas as pd

# 1. Input
raw_data = pd.read_csv("Menu.csv")
print(raw_data)                 #print table
print(raw_data.info())          #print table info

# 2. Process
total = raw_data["Price"].sum() #Calculate column sum

raw_data["Price"].var()                       #Calculate column Var
raw_data["Price"].std()                       #Calculate column std
raw_data["Price"].sort_values()               #Sort column by values
raw_data.sort_values("Price")                 #Sort column by values: show all columns
raw_data.sort_values("Price",ascending=False) #Sort column by values: descending order


# 3. Output
print(f"Total: {total}")
