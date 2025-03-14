#Imputation
import pandas as pd

NAN = pd.NA
data = {'id': [1, 2, NAN, 2, 3, 3, 4, 5, 5, NAN, 5, 6], 
        'Score': [10, 20, 20, NAN,30, 30, 40, 50, 50, 50, NAN, 60]}

df = pd.DataFrame(data)
print(df)
df_copy = df.copy()
df1 = df.copy()

for col in df_copy.columns:
    if df_copy[col].isnull().any():
        df_copy[col] = df_copy[col].fillna(df_copy[col].mean())
print(df_copy)
for col in df.columns:
    if df[col].isnull().any():
        df[col] = df[col].fillna(df[col].mode()[0])
print(df)
for col in df1.columns:
    if df1[col].isnull().any():
        df1[col] = df1[col].fillna(df1[col].median())

print(df1)