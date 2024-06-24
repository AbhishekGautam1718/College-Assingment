print("WELCOME TO 'ABHISHEK GAUTAM'F080' PROGRAM")
import numpy as np
a=[]
size= int(input("Please enter your size:"))
for i in range(size):
    val=int(input("Please enter your numbers:"))
    a.append(val)
arr=np.array(a)
sum=0
for i in range(size):
    sum=sum+a[i]
print(arr)
print("Your sum of all array element is:",sum)
print('*'*30)
print("THANK YOU FOR VISITING MY PROGRAM")
