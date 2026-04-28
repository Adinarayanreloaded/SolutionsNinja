def find_duplicate(arr):
    # Initialize the tortoise and hare
    tortoise = arr[0]
    hare = arr[0]
    
    # Phase 1: Finding the intersection point in the cycle
    while True:
        tortoise = arr[tortoise]  # Move tortoise by 1 step
        hare = arr[arr[hare]]  # Move hare by 2 steps
        if tortoise == hare:
            break
    
    # Phase 2: Finding the entry point to the cycle (which is the duplicate)
    tortoise = arr[0]
    while tortoise != hare:
        tortoise = arr[tortoise]
        hare = arr[hare]
    
    return tortoise