from sys import stdin

def sumOfTwoArrays(arr1, n, arr2, m, output):
    # Initialize pointers for the end of arr1 and arr2
    i = n - 1  # Pointer for the last element of arr1
    j = m - 1  # Pointer for the last element of arr2
    
    # Initialize the pointer for the last position of the output array
    k = max(n, m)  # The output array is of size max(n, m) + 1, so the last index is max(n, m)
    
    # Initialize carry to 0
    carry = 0  # This variable will store the carry for the addition of digits

    # Traverse both arrays from the end to the start as long as there are elements in both arrays
    while i >= 0 and j >= 0:
        # Calculate the sum of the digits from arr1 and arr2 along with the carry
        SUM = arr1[i] + arr2[j] + carry  # Add corresponding digits and the carry
        
        # Store the last digit of the sum in the current index of the output array
        output[k] = SUM % 10  # % 10 gives the unit place digit of the sum
        
        # Update the carry for the next addition
        carry = SUM // 10  # // 10 gives the carry for the next digit
        
        # Move to the previous digits
        i -= 1  # Move left in arr1
        j -= 1  # Move left in arr2
        k -= 1  # Move left in the output array

    # Process remaining digits of arr1 if arr2 is exhausted
    while i >= 0:
        # Add the current digit of arr1 and the carry
        SUM = arr1[i] + carry
        
        # Store the last digit of the sum in the current index of the output array
        output[k] = SUM % 10  # % 10 gives the unit place digit of the sum
        
        # Update the carry for the next addition
        carry = SUM // 10  # // 10 gives the carry for the next digit
        
        # Move to the previous digit
        i -= 1  # Move left in arr1
        k -= 1  # Move left in the output array

    # Process remaining digits of arr2 if arr1 is exhausted
    while j >= 0:
        # Add the current digit of arr2 and the carry
        SUM = arr2[j] + carry
        
        # Store the last digit of the sum in the current index of the output array
        output[k] = SUM % 10  # % 10 gives the unit place digit of the sum
        
        # Update the carry for the next addition
        carry = SUM // 10  # // 10 gives the carry for the next digit
        
        # Move to the previous digit
        j -= 1  # Move left in arr2
        k -= 1  # Move left in the output array
    
    # Handle the case where there might be a final carry
    output[0] = carry  # Place the final carry in the first position of the output array





#Standard I/O
def takeInput() :
    n = int(input()) 
    if n == 0 : 
        return list(), 0 
    arr = list(map(int, input().rstrip().split(" "))) 
    return arr, n 
def printList(arr, n) : 
    for i in range(n) : 
        print(arr[i], end = " ") 
    print() 
    
t = int(input().rstrip()) 
while t > 0 :
    arr1, n = takeInput()
    arr2, m = takeInput() 
    outputSize = (1 + max(n, m)) 
    output = outputSize * [0] 
    sumOfTwoArrays(arr1, n, arr2, m, output) 
    printList(output, outputSize) 
    
    t -= 1