def print_pattern(N):
    for i in range(N):
        # Calculate the starting character for the current row
        start_char = chr(65 + N - i - 1)  # ASCII code for 'A' is 65
        
        # Calculate the number of characters in the current row
        num_chars = i + 1
        
        # Generate the row
        row = ''.join(chr(ord(start_char) + j) for j in range(num_chars))
        
        # Print the row
        print(row)

# Example usage:
N = int(input())
print_pattern(N)
