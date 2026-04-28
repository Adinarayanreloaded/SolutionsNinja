def minimum_element(arr, n):
    # Initialize the minimum element with the first element of the array
    min_element = arr[0]
    
    # Iterate through the array and update the minimum element
    for i in range(1, n):
        min_element = min(min_element, arr[i])
    
    return min_element

# Input reading
n = int(input())
arr = list(map(int, input().split()))

# Call the function and print the result
print(minimum_element(arr, n))
