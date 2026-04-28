def arrange(arr, n):
    # Initialize pointers for the odd and even placements
    start = 0
    end = n - 1
    
    # Iterate through the numbers from 1 to N
    for i in range(1, n + 1):
        if i % 2 == 1:
            # Place odd numbers at the start
            arr[start] = i
            start += 1
        else:
            # Place even numbers at the end
            arr[end] = i
            end -= 1

# Read the number of test cases
t = int(input().strip())

# Process each test case
for _ in range(t):
    # Read the number of elements in the array
    n = int(input().strip())
    
    # Initialize the array with zeros
    arr = [0] * n
    
    # Call the function to arrange the elements
    arrange(arr, n)
    
    # Print the modified array
    print(" ".join(map(str, arr)))
