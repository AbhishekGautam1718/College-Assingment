#find array multiply and divide reminder:
print("WELCOME TO 'ABHISHEK GAUTAM',F080'PROGRAM")
def findArr(arr, size, R):
    Val = 1
    for i in range(size):
	    Val *= arr[i]
    return (Val % R)

size = int(input("Please Enter seze of the array: "))
arr = []
print("Please Enter elements of the array: ")
for i in range(size):
  num = int(input())
  arr.append(num)
D = int(input("Please Enter Your divisor Value: "))

rem = findArr(arr, size, D)
print('*'*40)

print("The remainder of array multiplication by divisor is ", rem)
print('THANK YOU')
