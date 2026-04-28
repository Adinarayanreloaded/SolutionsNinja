def print_pattern(N):
    for i in range(1, N + 1):
        if i == 1:
            pattern = "1"
        else:
            pattern = "1" + "2" * (i - 2) + "1"
        print(pattern)

# Read input from standard input
N = int(input().strip())
print_pattern(N)
