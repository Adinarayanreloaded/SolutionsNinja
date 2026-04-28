def merge(arr1, n, arr2, m):
    # Initialize the result array that will store the merged output
    result = []
    
    # Pointers for traversing arr1 and arr2
    i = 0
    j = 0

    # Traverse both arrays until we reach the end of one of them
    while i < n and j < m:
        if arr1[i] < arr2[j]:
            # If the current element of arr1 is smaller, append it to the result
            result.append(arr1[i])
            # Move the pointer of arr1 to the next element
            i += 1
        else:
            # If the current element of arr2 is smaller or equal, append it to the result
            result.append(arr2[j])
            # Move the pointer of arr2 to the next element
            j += 1

    # If there are remaining elements in arr1, append them to the result
    while i < n:
        result.append(arr1[i])
        i += 1

    # If there are remaining elements in arr2, append them to the result
    while j < m:
        result.append(arr2[j])
        j += 1

    # Return the merged and sorted array
    return result