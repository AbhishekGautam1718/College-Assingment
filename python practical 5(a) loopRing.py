def loopRing():
    start=int(input("Enter start integer:"))
    stop=int(input("Enter end integer:"))
    update=int(input("Enter update integer:"))
    for var in range(start,stop,update):
        print(var,end=",")
loopRing()
