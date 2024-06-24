#1D array 
import numpy as np
a=np.array([1,3,4,6])
print("array is:")
print(a)
b=a[0]
c=a[1]
d=a[2]
e=a[3]
print("index is:")
print(b,c,d,e)
print('**'*20)


#2D array
b=np.array([[4,3,5,6,7],[2,5,1,6,8]])
print("array is:")
print(b)
c=b[0,1]
d=b[0,3]
e=b[1,4]
f=b[0,4]
print("Indexing is:")
print(c,d,e,f)
print('**'*20)


#3D array
c=np.array([[[2,3,6,1,8,9],[2,1,5,4,6,5],[5,4,6,1,8,9]]])
print("array is:")
print(c)
d=c[0,1,2]
e=c[0,2,3]
f=c[0,1,2]
print("Indexing is:")
print(d,e,f)
print('**'*20)


#4D array
d=np.array([[[[1,5,4,3,6],[2,5,4,8,7],[4,7,9,8,6],[5,4,9,8,7]]]])
print("array is:")
print(d)
e=d[0,1,2,1]
print(e)
#ND array


n=np.array([4,5,7,8,6,1],ndmin=8)
print(n)
a=n[0]
print(a)
