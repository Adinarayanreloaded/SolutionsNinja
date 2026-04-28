def Remove_element(test_tuple):
    # Remove the last element using slicing
    return test_tuple[:-1]

# Read the number of elements in the tuple
n = int(input())
temp = []
for i in range(n):
    ans = input()
    temp.append(ans)

# Convert the list to a tuple
t = tuple(temp)

# Get the modified tuple after removing the last element
ans = Remove_element(t)

# Print the result
for i in ans:
    print(i, end=" ")
