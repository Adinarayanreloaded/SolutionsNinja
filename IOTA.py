
import sys

def intersections(arr1, n, arr2, m):
    """
    Print the intersection of two arrays/lists in the order they appear in the first array/list (arr1).
    
    Args:
    arr1 (List[int]): The first array/list of integers.
    n (int): The size of the first array/list.
    arr2 (List[int]): The second array/list of integers.
    m (int): The size of the second array/list.
    """
    from collections import Counter
    
    # Create a counter for the second array to keep track of occurrences
    counter_arr2 = Counter(arr2)
    
    result = []
    for num in arr1:
        if counter_arr2[num] > 0:
            result.append(num)
            counter_arr2[num] -= 1  # Decrease the count for the element
    
    print(' '.join(map(str, result)))

#Taking Input Using Fast I/O
def takeInput() :
    n = int(sys.stdin.readline().strip())
    if n == 0:
        return list(), 0

    arr = list(map(int, sys.stdin.readline().strip().split(" ")))
    return arr, n


#main
t = int(sys.stdin.readline().strip())

while t > 0 :
    arr1, n = takeInput()
    arr2, m = takeInput()

    intersections(arr1, n, arr2, m)
    print()

    t -= 1