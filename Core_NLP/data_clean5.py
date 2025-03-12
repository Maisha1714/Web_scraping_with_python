import polars as pl

data = {'id': [1, 2, 2, 2, 3, 3, 4, 5, 5, 5, 5, 6], 
        'Score': [10, 20, 20, 20, 30, 30, 40, 50, 50, 50, 50, 60]}

df = pl.DataFrame(data)
print(df)

print(df.shape[0])

dup = df.filter(df.is_duplicated())
print(dup.shape[0]) 

percentage = (dup.shape[0] / df.shape[0]) * 100
print('Percentage:', percentage, '%')

if percentage >= 50.00:
    print('Duplicate values are more than 50%')
    new_df = df.unique(keep="first")  
    print(new_df)
