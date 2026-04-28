def print_pattern(N):
    for i in range(N):
        if i == 0:
            print(1)
        else:
            # Print the first number
            print(i, end="")
            # Print (i-1) zeros
            for j in range(i-1):
                print(0, end="")
            # Print the last number
            print(i)

n = int(input())
print_pattern(n) 