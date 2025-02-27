import pandas as pd

data = {'id' : [1,2,2,3,4,5,5,6],'Scrore': [10,20,20,30,40,50,50,60]}
df = pd.DataFrame(data)
print(df)

dup = df.duplicated() #duplicate kine sheta check kore
print(dup)

f_df = df.drop_duplicates(keep = 'first') #duplicate value drop korar por
print(f_df)

l_df = df.drop_duplicates(keep = 'last') #duplicate value drop korar por
print(l_df)

