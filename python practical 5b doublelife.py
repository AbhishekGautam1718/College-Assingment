def BacteriaDoubleLife():
    time=0
    pop=int(input("Enter population of bacteria:"))
    rate=float(input("Enter growth rate:"))
    dub=pop*2
    pop=rate+dub
    print("population of bacteria:",pop)
    print("growth rate:",rate)
BacteriaDoubleLife()
