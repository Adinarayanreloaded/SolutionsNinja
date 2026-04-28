def find_missing_and_repeating(arr):
    n = len(arr)
    repeating = -1
    missing = -1
    
    # Mark the visited elements by negating the value at index equal to the element's value
    for i in range(n):
        if arr[abs(arr[i]) - 1] < 0:
            repeating = abs(arr[i])
        else:
            arr[abs(arr[i]) - 1] = -arr[abs(arr[i]) - 1]
    
    # Find the missing number
    for i in range(n):
        if arr[i] > 0:
            missing = i + 1
    
    return missing, repeating