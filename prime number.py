n=int(input("Enter your number:"))
count=0
i=1
while (n>=i):
    if (n%i==0):
        count=count+1
    i=i+1
if (count==2):
    print("Prime number:")
else:
    print("composit number:")
