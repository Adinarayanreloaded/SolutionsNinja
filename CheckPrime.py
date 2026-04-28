def check_prime(num):
    # Edge case: numbers less than or equal to 1 are not prime
    if num <= 1:
        return False
    # 2 and 3 are prime numbers
    if num <= 3:
        return True
    # Multiple of 2 or 3 are not primes
    if num % 2 == 0 or num % 3 == 0:
        return False
    # Check for other divisors from 5 to sqrt(num)
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

