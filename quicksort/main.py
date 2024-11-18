from typing import List


def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[:] if x > pivot]

    return quicksort(left) + [pivot] + quicksort(right)

print(quicksort([1,5,2,3,7,0]))