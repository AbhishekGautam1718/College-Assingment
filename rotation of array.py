# Function to rotate arrays in Python
print("WELCOME TO 'ABHISHEK GAUTAM,F080'PROGRAM")
def rotateArrayLeft(arr, R, n):
    for i in range(R):
    	firstVal = arr[0]
    	for i in range(n-1):
    		arr[i] = arr[i+1]
    	arr[n-1] = firstVal

# Taking array input from user
arr = [1, 2, 3, 4, 5, 6, 7]
n = int(input("Please Enter Size of the array: "))
arr = []
print("Please Enter elements of the array :")
for i in range(n):
  numbers = int(input())
  arr.append(numbers)
R = int(input("Please Enter rotation count: "))

# Printing array 
print("Your Initial Array :", end = " ")
for i in range(n):
	print ("%d"% arr[i],end=" ")
	
# Calling function for left Rotating array 
rotateArrayLeft(arr, R, n)

# Printing new array 
print("\nYour Array after rotation: ", end = " ")
for i in range(n):
	print ("%d"% arr[i],end=" ")
print()
print('TAHNK YOU')
