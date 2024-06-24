def loopRange():
    print("Number from 0 to 4:")
    for i in range(5):
        print(i)
    print("~"*30)
    print("Number for 100 to 110:")
    for j in range(100,110):
        print(j)
    print("~"*30)
    print("Even number from 10 to 20:")
    for x in range(10,21,2):
        print(x)
    print("~"*30)
    print("Reverse number from 20 to 10:")
    for a in range(20,9,-1):
        print(a)
    print("~"*30)
    print("Number from -1 to -10:")
    for b in range(-1,-11,-1):
        print(b)
if __name__=="__main__":
    loopRange()
