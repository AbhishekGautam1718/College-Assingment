def inputdata():
    name=str(input("Enter your name:"))
    p=float(input("principal ammount:"))
    n=int(input("number of months:"))
    r=int(input("rate of intrest (per month):"))
    calSI(name,p,n,r)
def calSI(name,p,n,r):
    SI=(p*n*r)/100
    amt=SI+p
    display(name,p,n,r,SI,amt)    
def display(name,p,n,r,SI,amt):
    print("~~~"*20)
    print("name:",name)
    print("principal ammount:Rs.",p)
    print("number of months:",n)
    print("rate of intrest:",r,"per months")
    print("simple intrest:Rs.",SI)
    print("Total Ammount:RS.",amt)
if __name__=="__main__":
    inputdata()

    
    
    

        
            
