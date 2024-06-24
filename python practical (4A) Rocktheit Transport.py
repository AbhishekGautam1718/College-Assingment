def rocktheit ():
    name=str(input("Enter your name:"))
    w=int(input("to store the weight of the parcel in kg:"))
    if w>=0 and w<=10:
        cal=w*25
        print("calculate:",cal)
    elif w>=10 and w<=20:
        cal=w*20
        print("calculate:",cal)
    elif w>=20 and w<=30:
        cal=w*10
        print("calculate:",cal)
    else:
        print("wrong input:")
    Total=5/100*cal+cal
    print("Total value including 5% surcharge:",Total)
    display(name,w,cal,Total)
def display(name,w,cal,Total):
    print("~~"*40)
    print("name:",name)
    print("to store the weight of the parcel(in kg)",w)
    print("calculate:",cal)
    print("Total value including 5% surcharge:",Total)
    
    
    
rocktheit()
