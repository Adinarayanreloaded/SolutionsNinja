from sys import stdin
#MIN_VALUE = -2147483648


def secondLargestElement(arr, n):
    if n < 2:
        return None  # Not enough elements to determine the second largest
    
    # Sorting the array in descending order
    arr.sort(reverse=True)
    
    # Find the second largest unique element
    largest = arr[0]
    for i in range(1, n):
        if arr[i] != largest:
            return arr[i]
    
    return None  # In case all elements are the same
    
def takeInput() :
    n = int(stdin.readline().rstrip())
    if n != 0:
        arr = list(map(int, stdin.readline().rstrip().split(" ")))
        return arr, n

    return list(), 0


#main
arr, n = takeInput()
print(secondLargestElement(arr, n))
