def divide(x, y):
    try:
        # Attempting to perform the division
        result = x // y
        print(result)
    except ZeroDivisionError:
        # Handling division by zero
        print("Sorry ! You are dividing by zero")
    finally:
        # This block always executes
        print("This is always executed")

# Taking two integer inputs
x = int(input())
y = int(input())

# Calling the divide function and printing the result
result = divide(x, y)

