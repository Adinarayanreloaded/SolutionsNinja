
import sys

def duplicateNumber(arr, n):
    xor_sum = 0
    
    # XOR all numbers from 0 to N-2
    for i in range(n - 1):
        xor_sum ^= i
    
    # XOR all elements in the array
    for num in arr:
        xor_sum ^= num
    
    # The result is the duplicate number
    return xor_sum






















#Taking Input Using Fast I/O
def takeInput() :
    n = int(sys.stdin.readline().strip())

    if n == 0 :
        return list(), 0

    arr = list(map(int, sys.stdin.readline().strip().split()))
    return arr, n


#main
t = int(sys.stdin.readline().strip())

while t > 0 :
    
    arr, n = takeInput()
    print(duplicateNumber(arr, n))

    t -= 1
    