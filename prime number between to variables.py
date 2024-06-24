print("Welcome to 'Abhishek Gautam',Roll no.F080, program")
start = int(input(" Please Enter the Start Value: "))
limit = int(input(" Please Enter the Limit Value: "))

N = start

while(N <= limit):
    count = 0
    i = 2
    
    while(i <= N//2):
        if(N % i == 0):
            count = count + 1
            break
        i = i + 1

    if(count == 0 and N != 1):
        print(" %d" %N, end = '  ')
    N = N  + 1

