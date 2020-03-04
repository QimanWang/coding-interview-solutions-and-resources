'''
bubble biggest number to right each iteration
'''

def bubbleSort(array):
    isSorted = False
    # how many sorted so far
    counter = 0
    while not isSorted:
        isSorted = True
        for i in range(len(array)-1-counter):
            if array[i] > array[i+1]:
                swap(i, i+1, array)
                isSorted = False
        counter += 1
    return array


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]


ary = [5, -2, 2, -8, 3, -10, -6, -1, 2, -2, 9, 1, 1]
print(bubbleSort(ary))
