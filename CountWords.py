def countWords(s):
    if not s:  # Edge case for empty string
        return 0
    
    count = 1  # Start with 1 if the string is not empty
    for char in s:
        if char == ' ':  # Increment count for each space
            count += 1
    return count