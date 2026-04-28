def print_pattern(N):
    for i in range(1, N + 1):
        # Generate the pattern for each row
        pattern = ''.join(str(j) for j in range(i, 0, -1))
        print(pattern)

# Reading input from standard input (you can modify this part based on how you input N)
N = int(input().strip())
print_pattern(N)
