import polars as pl

data = {'id' : [1,2,2,3,4,5,5,6],'Scrore': [10,20,20,30,40,50,50,60]}
df = pl.DataFrame(data)
print(df)

dup = df.filter(pl.col('id').is_duplicated()) #duplicate kine sheta check kore
print(dup)

f_df = df.unique() #duplicate value drop korar por
print(f_df)

l_df = df.unique(keep = 'last') #duplicate value drop korar por
print(l_df)

