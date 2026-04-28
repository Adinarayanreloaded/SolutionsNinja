from sys import stdin

def countTriplets(arr, n, x):
    # Sort the array
    arr.sort()
    count = 0
    # Iterate over the array
    for i in range(n - 2):
        # Initialize two pointers
        left = i + 1
        right = n - 1
        
        # Use two pointers to find the triplet
        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]
            
            if current_sum == x:
                count += 1
                left += 1
                right -= 1
            elif current_sum < x:
                left += 1
            else:
                right -= 1
    
    # Return the count of triplets
    return count

def countTripletsAllCombinations(arr, n, x):
    count = 0
    
    # Iterate over each triplet combination
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if arr[i] + arr[j] + arr[k] == x:
                    count += 1

    return count

# Taking Input Using Fast I/O
def takeInput():
    n = int(stdin.readline().strip())

    if n == 0:
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split()))
    return arr, n

# Main
t = int(stdin.readline().strip())

while t > 0:
    arr, n = takeInput()
    x = int(stdin.readline().strip())
    result = countTripletsAllCombinations(arr, n, x)
    print(result)
    t -= 1
