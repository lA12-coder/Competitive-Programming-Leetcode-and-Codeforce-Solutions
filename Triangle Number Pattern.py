n=5
# Normal Triangle
for row in range(1,n+1):
    for col in range(1,row+1):
        print(col,end=' ')
    print(end='\n')


#Inverted Triangle
for row in range(1, n+1):
    print(' ' * (row-1),end='')
    for col in range(row,n+1):
        print(col,end='')
    print(end='\n')

