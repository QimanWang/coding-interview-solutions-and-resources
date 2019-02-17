'''
store the 3 largest num
'''

def findThreeLargestNumbers(array):
    threeLargest = [None]*3

    # go thru the num ary and update the 3 nums
    for num in array:
        updateLargest(largest, num)
    return threeLargest

def updateLargest(threeLargest, num):
    if threeLargest[2] is None or num > threeLargest[2]:
        shiftAndUpdate(threeLargest, num,2)
    elif threeLargest[1] is None or num > threeLargest[1]:
        shiftAndUpdate(threeLargest, num 1)
    elif threeLargest[0] is None or num > threeLargest[0]:
        shiftAndUpdate(threeLargest, num 0)
    
def shiftAndUpdate(array, num, idx):
    
    # the for will stop on the idx and update with numebr we want to replace,
    # the i's before that will be updated with val from i+1
    for i in range( idx + 1):
        if i == idx:
            array[i] = num
        else:
            array[i] = array[i+1]

