import polars as pd

data = {'id' : [1,2,2,2,3,3,4,5,5,5,5,6],'Scrore': [10,20,20,20,30,30,40,50,50,50,50,60]}
df = pd.DataFrame(data)
print(df)
print(df.count())

dup = df[df.duplicated()] #duplicate kine sheta check kore
print(dup.count())
percentage = (dup.count()/df.count())*100
print('Percentage : \n',percentage)

if (percentage >= 50.00).any():
    print('Duplicate values are more than 50%')
    new_df = df.drop_duplicates(keep = 'first') #duplicate value drop korar por
    print(new_df)
