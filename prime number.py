n=int(input("Enter Number:"))
count=0
for i in range(1,n+1):
    
    if(n%i==0):
        
        count=count+1
    i=i+1
if(count==2):
        print("prime number:")

else:
        print("Not prime:")
