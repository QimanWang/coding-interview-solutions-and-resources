# def selectionSort(array):
#     # Write your code here.
#     # for each postion of ary:
#                 # we will go over that postyion and all afterwards to find smallest,
#                 # move smallest to that postion.
#     counter = ''
#     for i in range(len(array)):
#         smallest_idx = i
#         for j in range(i+1, len(array)):
#             if array[j] < array[smallest_idx]:
#                 smallest_idx = j
#         if smallest_idx != i:
#             swap(array, smallest_idx, i)

#     return array


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]

    '''
	i= 0, 1,.... 12
	small = 0
	j= 1,2,...,12
	
	
	
	'''


def selectionSort(array):
    # Write your code here.
    # for each postion of ary:
                # we will go over that postyion and all afterwards to find smallest,
                # move smallest to that postion.
    currIdx = 0
    while currIdx < len(array)-1:
        smallest_idx = currIdx
        for j in range(currIdx+1, len(array)):
            if array[j] < array[smallest_idx]:
                smallest_idx = j

        swap(array, smallest_idx, currIdx)
        currIdx += 1
    return array


# print(selectionSort([2, -3, 1, 0, -9]))
ary = [1, 2, 3]
print("z".join(str(ary)))
