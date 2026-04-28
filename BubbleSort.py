from typing import List

def bubbleSort(arr, n):
    for i in range(n-1):
        # Track if any swaps were made in this pass
        swapped = False
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                # Swap if the element found is greater than the next element
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        # If no elements were swapped, the array is already sorted
        if not swapped:
            break
        pass