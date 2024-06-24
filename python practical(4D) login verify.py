count = 0
def login_verify(login,password):
    global count
    count=count + 1
    if count == 3:
        print("No more attemps allowed ! ")
    else:
        if login == "Abhishek" and password == "Gautam@" :
            print('Login Successful to ABHISHEK')
        else:
            print("Login Unsuccessful ! Login id or password not matched ")
            exit_continue()
    
def inputDetail():
    l = input("Enter login id : ")
    p = input("Enter password : ")
    # calling function login_verify()
    login_verify(l,p)
    
def exit_continue():
    print("Yes : Continue\nNo : Exit")
    val = input("Enter your choice : ")
    if val == "Yes" or val =="yes" or val == "YES":
        inputDetail() 
    elif val == "No" or val =="no" or val == "NO":
        print("Thank You")
    else :
        print("Wrong Input! Try Again")
        exit_continue()

inputDetail()



