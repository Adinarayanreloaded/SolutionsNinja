class MyClass:
    def __init__(self):
        pass  # No specific initialization required

    def get_max_value(self, x, y):
        # Returns the maximum of x and y
        return max(x, y)


# Read two integers from user input
x = int(input())
y = int(input())

# Create an instance of MyClass
obj = MyClass()

# Call the instance method get_max_value and print the result
print(obj.get_max_value(x, y))
