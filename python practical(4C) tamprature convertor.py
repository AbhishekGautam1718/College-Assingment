if __name__=="__main__":
    print("~~~Temprature Convertor~~~")
    print("1--> Fahrenheit to Celsius")
    print("2--> Celsius to Fahrenheit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        fah=int(input("Enter value for Fahrenheit:"))
        Cel=(fah*9/5)+32
        print("Fahrenhiet:",fah,"=",Cel,"celsius:")
    elif choice==2:
        Cel=int(input("Enter value for Celsius:"))
        fah=(Cel-32)*5/9
        print("Celsius:",Cel,"=",fah,"Fahrenhiet:")
    else:
        print("wrong input")

