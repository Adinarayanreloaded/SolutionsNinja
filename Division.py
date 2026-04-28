def perform_division():
    try:
        # Taking two integer inputs
        num1 = int(input())
        num2 = int(input())
        
        # Attempting to perform integer division
        result = num1 // num2
        print(result)
    except ZeroDivisionError:
        # Handling division by zero
        print("Division not possible")
    finally:
        # This block always executes
        print("Hey you are doing division")

# Calling the function to perform the task
perform_division()
