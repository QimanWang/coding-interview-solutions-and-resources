'''
scan array for smallest, place in front, then repeat for each following positions
'''

def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


def selectionSort(array):
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
