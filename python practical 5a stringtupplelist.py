def ListTuppleString():
    name=input("Enter your name:")
    a=(1,5,6,4,3,8)
    b=[2,5,6,8,7,9]
    c=("abhishek","ranesh","hkahdfjf")
    for i in a:
        print(a)
    for i in b:
        print(b) 
    for i in c:
        print(c)
        display(name,a,b,c)
       
def display(name,a,b,c):
    print("~~"*30)
    print("Enter your name:",name)
    print("tupple value",a)
    print("list value",b)
    print("string value",c)

ListTuppleString()
    
