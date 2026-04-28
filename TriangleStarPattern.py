def print_pattern(N):
    for i in range(1, N + 1):
        print('*' * i)

# Reading input from standard input (you can modify this part based on how you input N)
N = int(input().strip())
print_pattern(N)
