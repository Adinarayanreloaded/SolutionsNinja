from sys import stdin

def rotate(arr, n, d):
    # Handle edge cases where d is 0 or n
    if n == 0 or d % n == 0:
        return
    
    d = d % n  # In case d is greater than n
    
    # Step 1: Store the first d elements in a temporary list
    temp = arr[:d]
    
    # Step 2: Shift the remaining elements of the array to the left
    for i in range(d, n):
        arr[i - d] = arr[i]
    
    # Step 3: Copy the elements from the temporary list to the end of the array
    for i in range(d):
        arr[n - d + i] = temp[i]


#Taking Input Using Fats I/O
def takeInput() :
    n = int(stdin.readline().rstrip())
    if n == 0:
        return list(), 0

    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n


#to print the array/list 
def printList(arr, n) : 
    for i in range(n) :
        print(arr[i], end = " ")
    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :
    
    arr, n = takeInput()
    d = int(stdin.readline().rstrip())
    rotate(arr, n, d)
    printList(arr, n)
    
    t -= 1