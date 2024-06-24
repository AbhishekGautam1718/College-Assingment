import numpy as np
matrix=[]
row=int (input("Enter numbers of row:"))
col=int(input("Enter numbers of colom:"))
for i in range(row):
    a=[]
    for i in range(col):
        v=int(input("Enter your number:"))
        a.append(v)
    matrix.append(a)
arr=np.array(matrix)
for i in range(row):
    for j in range(col):
        print(arr[i][j],end=' ')
    print()
print(type(arr))
