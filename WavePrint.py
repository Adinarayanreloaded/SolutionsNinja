def wavePrint(input_array):
    if not input_array or not input_array[0]:
        return
    
    rows = len(input_array)
    cols = len(input_array[0])
    result = []

    for j in range(cols):
        if j % 2 == 0:
            # Print top to bottom for even-indexed columns
            for i in range(rows):
                result.append(input_array[i][j])
        else:
            # Print bottom to top for odd-indexed columns
            for i in range(rows - 1, -1, -1):
                result.append(input_array[i][j])

    print(" ".join(map(str, result)))

# Example usage:
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    rows, cols = map(int, data[0].split())
    input_array = []
    
    for i in range(1, rows + 1):
        row = list(map(int, data[i].split()))
        input_array.append(row)
    
    wavePrint(input_array)
