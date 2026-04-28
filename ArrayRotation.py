
from sys import stdin

def arrayRotateCheck(arr, n):
    """
    Find the rotation index K of a sorted and rotated array.
    This function uses binary search to find the smallest element in the array.
    The index of this smallest element is the number of positions the array was rotated.

    :param arr: The rotated sorted array.
    :param n: The number of elements in the array.
    :return: The index where the array was rotated.
    """
    if n == 0:
        return 0  # Empty array edge case (not applicable as per constraints N >= 2)

    # Initialize the binary search pointers
    low, high = 0, n - 1
    
    # Perform binary search to find the rotation index
    while low < high:
        mid = (low + high) // 2
        
        # Check if the middle element is greater than the high element
        if arr[mid] > arr[high]:
            # The smallest element is in the right half
            low = mid + 1
        else:
            # The smallest element is in the left half or at mid
            high = mid
    
    # When low == high, this index points to the smallest element
    return low


#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().rstrip())
    if n == 0:
        return list(), 0

    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n


#main
t = int(stdin.readline().rstrip())

while t > 0 :

    arr, n = takeInput()
    print(arrayRotateCheck(arr, n))

    t -= 1