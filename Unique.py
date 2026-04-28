import sys

def findUnique(arr, n):
    unique_num = 0  # Initialize the unique number as 0
    
    for num in arr:
        unique_num ^= num  # Apply XOR operation with each number
    
    return unique_num  # The result after XORing all numbers


#Taking Input Using Fast I/O
def takeInput() :
    n = int(sys.stdin.readline().rstrip())

    if n == 0 :
        return list(), 0

    arr = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    return arr, n


#main
t = int(sys.stdin.readline().rstrip())

while t > 0 :

    arr, n = takeInput()
    print(findUnique(arr, n))

    t -= 1