def printTable(start, end, step):
    # Iterate from start to end with step size
    fahrenheit = start
    while fahrenheit <= end:
        # Calculate Celsius using the formula and print both values
        celsius = (5 / 9) * (fahrenheit - 32)
        # Print Fahrenheit and the integer part of Celsius
        print(fahrenheit, int(celsius))
        # Increment fahrenheit by step
        fahrenheit += step

# Example usage (input already handled as per problem statement)
s = int(input())
e = int(input())
w = int(input())
printTable(s, e, w)
