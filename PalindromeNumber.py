def palindromeNumber(n: int) -> bool:
    # Convert number to string to handle negative numbers easily
    str_n = str(n)
    
    # Handle negative numbers
    if str_n[0] == '-':
        return False
    
    # Check if the string representation is the same forwards and backwards
    return str_n == str_n[::-1]
