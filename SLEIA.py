from sys import stdin
#MIN_VALUE = -2147483648

def secondLargestElement(arr, n):
    # Handle edge case where there are fewer than 2 elements
    if n < 2:
        return None  # or appropriate value indicating no second largest element
    
    # Initialize the largest and second largest elements
    first = second = float('-inf')

    # Traverse the array
    for i in range(n):
        # Update the largest and second largest elements
        if arr[i] > first:
            second = first
            first = arr[i]
        elif arr[i] > second and arr[i] != first:
            second = arr[i]
    
    # If second is still negative infinity, it means there was no second largest element
    if second == float('-inf'):
        return None  # or appropriate value indicating no second largest element
    
    return second



def takeInput() :
    n = int(stdin.readline().rstrip())
    if n != 0:
        arr = list(map(int, stdin.readline().rstrip().split(" ")))
        return arr, n

    return list(), 0


#main
arr, n = takeInput()
print(secondLargestElement(arr, n))
