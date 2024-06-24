size1=int(input("Please Enter Your First List Size:"))
a=[]
for i in range(size1):
    L1=int(input("Please Enter Your elements:"))
    a.append(L1)
print(a)
    
size2=int(input("Please Enter Your Second List Size:"))
b=[]
for i in range(size2):
    
    L2=int(input("Please Enter Your elements:"))
    b.append(L2)
print(b)

A=list(set(a)|set(b))
B=list(set(a)&set(b))

print('Union of the arrays:',A)
print('intersection of the arrays:',B)
