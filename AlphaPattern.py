def print_pattern(N):
    for i in range(1, N + 1):
        pattern = chr(64 + i) * i
        print(pattern)

# Read input from standard input
N = int(input().strip())
print_pattern(N)
