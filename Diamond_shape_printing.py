print("Diamand Shape printing in form of star")
n=int(input("Enter Your Number for pattern:"))#please enter atleast 2 number
for i in range(n):
    print(' '*(n-i-1)+'* '*(i+1))
for i in range(n-1):
    print(' '*(i+1)+'* '*(n-i-1))
    
