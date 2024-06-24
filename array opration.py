import numpy as np
matrix1=[]
Row=int(input('Please Enter your Row of matrix :'))
col=int(input('Please Enter your colom of matrix value:'))

for i in range(Row):
    a=[]
    for j in range(col):
        val=int(input("Please Enter your matrix value"))
        a.append(val)
    matrix1.append(a)
arr=np.array(matrix1)
for i in range(Row):
    for j in range(col):
        print(arr[i][j],end=' ')
    print()

print('*'*40)

matrix2=[]
Row=int(input('Please Enter your Row of matrix :'))
col=int(input('Please Enter your colom of matrix value:'))

for i in range(Row):
    a=[]
    for j in range(col):
        val=int(input("Please Enter your matrix value"))
        a.append(val)
    matrix2.append(a)
arr=np.array(matrix2)
for i in range(Row):
    for j in range(col):
        print(arr[i][j],end=' ')
    print()
# for subtracat matrix:
    matrix3 = []
    for i in range(Row):
        matrix3.append([])
        for j in range(col):
            sub = matrix1[i][j] - matrix2[i][j]
            matrix3[i].append(sub)

    print("\nSubtraction Result:")
    for i in range(Row):
        for j in range(col):
            print(matrix3[i][j], end=" ")
        print()




 # for multiplication matrix:
    matrix4 = []
    for i in range(Row):
        matrix4.append([])
        for j in range(col):
            mul = matrix1[i][j] * matrix2[i][j]
            matrix4[i].append(mul)

    print("\nMultiplication Result:")
    for i in range(Row):
        for j in range(col):
            print(matrix3[i][j], end=" ")
        print()

        
# adding matrices
print("mat1+mat2...")
print(matrix1+matrix2)
print("np.add(mat1,mat2)...")
print(np.add(matrix1,matrix2))
print()

# producting matrices
print("np.dot(mat1,mat2)...")
print(np.dot(matrix1,matrix2))
print() # prints newline

# Square root of matrix1 elements
print("np.sqrt(mat1)...")
print(np.sqrt(matrix1))
print()

# Square root of matrix2 elements
print("np.sqrt(mat2)...")
print(np.sqrt(matrix2))
print() 
