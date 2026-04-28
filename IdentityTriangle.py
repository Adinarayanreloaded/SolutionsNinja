def classify_triangle(X, Y, Z):
    # Check the triangle inequality conditions
    if X + Y > Z and X + Z > Y and Y + Z > X:
        # Check for the type of triangle
        if X == Y == Z:
            print("Equilateral Triangle")
        elif X == Y or X == Z or Y == Z:
            print("Isosceles Triangle")
        else:
            print("Scalene Triangle")
    else:
        print("Not a Triangle")

# Example usage:
# Read inputs from the user or use predefined values for testing
X = int(input().strip())
Y = int(input().strip())
Z = int(input().strip())

# Call the function to classify the triangle based on sides X, Y, Z
classify_triangle(X, Y, Z)
