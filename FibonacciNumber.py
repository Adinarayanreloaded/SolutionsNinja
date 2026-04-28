def checkMember(n):
    if n < 0:
        return False

    # Initialize first two Fibonacci numbers
    a, b = 0, 1
    
    # Generate Fibonacci numbers until we either match `n` or surpass it
    while a <= n:
        if a == n:
            return True
        a, b = b, a + b

    return False
