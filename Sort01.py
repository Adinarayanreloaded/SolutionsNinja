from sys import stdin

def sortZeroesAndOne(arr, n):
    left = 0  # Pointer for the next position of 0
    
    # Traverse the array
    for i in range(n):
        if arr[i] == 0:
            # Swap if we find a 0
            arr[left], arr[i] = arr[i], arr[left]
            left += 1  # Move the left pointer to the next position


#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().strip())

    if n == 0 :
        return list(), 0

    
    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


def printList(arr, n) :
    for i in range(n) :
        print(arr[i], end = ' ')
    print()


#main
t = int(stdin.readline().strip())

while t > 0 :
    
    arr, n = takeInput()
    sortZeroesAndOne(arr, n)
    printList(arr, n)
    print()

    t -= 1