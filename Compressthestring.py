from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

def getCompressedString(s):
    # If the input string is empty, return an empty string
    if not s:
        return ""

    # List to store the compressed version of the string
    compressed_string = []
    
    # Initialize the count for the first character
    count = 1

    # Iterate through the string starting from the second character
    for i in range(1, len(s)):
        # Check if the current character is the same as the previous one
        if s[i] == s[i - 1]:
            # Increment the count if the characters are the same
            count += 1
        else:
            # Append the previous character to the result
            compressed_string.append(s[i - 1])
            # If the count is greater than 1, append the count to the result
            if count > 1:
                compressed_string.append(str(count))
            # Reset the count for the new character
            count = 1

    # Handle the last character after the loop
    compressed_string.append(s[-1])
    if count > 1:
        compressed_string.append(str(count))

    # Join the list into a single string and return it
    return ''.join(compressed_string)

    
    compressed_string = []
    count = 1
    
    # Traverse through the string
    for i in range(1, len(input)):
        if input[i] == input[i - 1]:
            count += 1  # Increase the count for consecutive characters
        else:
            # Append the previous character and its count if > 1
            compressed_string.append(input[i - 1])
            if count > 1:
                compressed_string.append(str(count))
            count = 1  # Reset count for the new character
    
    # Handle the last group of characters
    compressed_string.append(input[-1])
    if count > 1:
        compressed_string.append(str(count))
    
    return ''.join(compressed_string)



# Main.
string = stdin.readline().strip();
ans = getCompressedString(string)
print(ans)