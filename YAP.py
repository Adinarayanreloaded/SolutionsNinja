def ninjaPuzzle(N):
    result = []
    for i in range(N):
        spaces = ' ' * i
        stars = '*' * (N - i)
        result.append(spaces + stars)
    
    # Output each line
    for line in result:
        print(line)