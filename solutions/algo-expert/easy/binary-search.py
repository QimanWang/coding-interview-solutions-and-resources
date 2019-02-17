# get the leftr, rigfht idx, then update the idx with middle

def binarySearch(array, target):
    # Write your code here.
	left , right = 0,len(array)-1
	
	while left <= right:
		middle = (left+right)//2
		if array[middle] == target:
			return middle		
		elif array[middle] < target:
			left = middle+1
		else:
			right = middle-1
	return -1