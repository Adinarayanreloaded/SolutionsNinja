def print_pattern(N):
    for i in range(N, 0, -1):
        pattern = ''.join(str(num) for num in range(1, i+1))
        print(pattern)

# Read input from standard input
N = int(input().strip())
print_pattern(N)
