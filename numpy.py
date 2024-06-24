
    
import numpy as np
a=[]
f=int(input("Enter your size:"))
for i in range(f):
    var=int(input("Enter your number:"))
    a.append(var)
myarray=np.array(a)
print(myarray)
