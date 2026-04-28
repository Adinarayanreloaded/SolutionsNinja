def check_palindrome(s):
    # Initialize an empty string to store only alphanumeric characters
    filtered_string = ''
    
    # Iterate over each character in the string
    for char in s:
        # Manually check if the character is alphanumeric and convert to lowercase
        if 'a' <= char <= 'z' or '0' <= char <= '9':
            filtered_string += char
    
    # Initialize two pointers
    left, right = 0, len(filtered_string) - 1
    
    while left < right:
        if filtered_string[left] != filtered_string[right]:
            return False
        left += 1
        right -= 1
    
    return True
