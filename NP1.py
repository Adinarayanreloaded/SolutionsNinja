def print_pattern(N):
    for i in range(1, N + 1):
        pattern = '1' * i
        print(pattern)

# Read input from standard input
N = int(input().strip())
print_pattern(N)
