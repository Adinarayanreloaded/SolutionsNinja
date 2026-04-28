def print_pattern(N):
    for i in range(N):

        start_char = chr(65 + i)  # ASCII code for 'A' is 65
        num_chars = i + 1
        row = ''.join(chr(ord(start_char) + j) for j in range(num_chars))
        print(row)

# Example usage:
N = int(input())
print_pattern(N)
