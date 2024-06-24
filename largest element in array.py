print("WELCOME TO 'ABHISHEK GAUTAM,F080'PROGRAM")
def FindLargestElement(arr,n):
	maxVal = arr[0]

	for i in range(1, n):
		if arr[i] > maxVal:
			maxVal = arr[i]
	return maxVal

# code to take user input for the array...
size = int(input("Please Enter you size of elements in the array: "))
arr = []
print("Please Enter elements of the array: ")
for i in range(size):
  num = int(input())
  arr.append(num)
  
# Calling the method to find the largest value  
maxVal = FindLargestElement(arr,size)
print ("Largest in given array is",maxVal)
print('*'*40)
print('THANK YOU')
