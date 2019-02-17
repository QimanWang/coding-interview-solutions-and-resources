'''
we assume idx 0 is sorted. we partition the rest as a unsorted list
for each num in unsorted:
    we will insert to the end of sorted.
    then move the value to the right place.
'''


def insertionSort(array):

    # assume idx 0 is sorted
    for i in range(1, len(array)):
        j = i
        # while out of order, and j is valid
        while j > 0 and array[j] < array[j-1]:
            swap(j, j-1, array)
            j -= 1
    return array


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]


print(insertionSort([-3, -6, 10, -2, 1, 4, -1, 0, -2]))
