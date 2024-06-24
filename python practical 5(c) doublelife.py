def Doublelife():
    time=0
    pop=int(input("Enter population of Bacteria:"))
    rate=int(input("Enter increase rate of pop:"))
    dobpop=pop*2
    while pop<=dobpop:
        pop=pop+(pop*rate)
        time=time+1
        print("Bacteria population:",round(pop))
        print("Bacteria double time:",time,"sec.")
def whileloop():
    limit=int(input("Enter the limit:"))
    start=int(input("Enter the start:"))
    l=limit
    s=start
    #printing numbers
    print("Natural numbers:")
    while l<=limit:
        print(l)
        l=l+1
        print('~~'*20)
        print()
Doublelife()
