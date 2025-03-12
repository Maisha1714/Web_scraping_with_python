import polars as pl

data = {'id': [1, 2, None, 2, 3, 3, 4, 5, 5, None, 5, 6], 
        'Score': [10, 20, 20, 20,30, 30, 40, 50, 50, 50, 50, 60]}

df = pl.DataFrame(data)
rmv_row = df.drop_nulls()
rmv_col = df.select(col for col in df.columns if not df[col].null_count())
print(df)
print(rmv_row)
print(rmv_col)