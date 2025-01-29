values = []
for i in range(1,1001): #comment page patter for 1-1000
    if i>=4 and i<1000:
        j=4
        values.append(j)
    elif i==1000:
        values.append(5)
    else:
        values.append(i)

print(values) #1 2 3 4 ..................5

