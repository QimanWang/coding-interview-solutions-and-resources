'''
at least 1 pair exist
[first-ary-num,second-ary-num]
abs(first-ary-num - second-ary-num) <= abs(first-ary[i] - second-ary[j])
where i in range(0,len(ary1)) j in range(0,len(ary2)

if we do brute forcce and compare every pair, it will be o(ij)
where every pair is compred.

if we sort, it will be o(ilog(i) + jlog(j))
sorting both array, then have move some pointers

what are these pointers?
                                                       
'''


def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    arrayOne.sort()
    arrayTwo.sort()

    idxOne = 0
    idxTwo = 0
    smallestPair = []

    min_diff = float("inf")
    while idxOne < len(arrayOne) and idxTwo < len(arrayTwo):

        firstNum = arrayOne[idxOne]
        secondNum = arrayTwo[idxTwo]
        new_diff = abs(firstNum - secondNum)

        # update diff if new diff is smaller
        if new_diff < min_diff:
            min_diff = new_diff
            smallestPair = [firstNum, secondNum]

        if firstNum < secondNum:
            idxOne += 1
        elif secondNum < firstNum:
            idxTwo += 1
        else:
            return smallestPair
    return smallestPair
