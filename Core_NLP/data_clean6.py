#missing value handle :
#removing rows or column
#Imputation : filling values with mean, median, mode
#Propagation : forward propagation, backward propagation
#Interpolation : linear, polynomial, spline

import pandas as pd

NAN = pd.NA
data = {'id': [1, 2, NAN, 2, 3, 3, 4, 5, 5, NAN, 5, 6], 
        'Score': [10, 20, 20, 20,30, 30, 40, 50, 50, 50, 50, 60]}

df = pd.DataFrame(data)
rmv_row = df.dropna()
rmv_col = df.dropna(axis = 1)
print(df)
print(rmv_row)
print(rmv_col)