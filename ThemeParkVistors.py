def categorize_visitor(age):
    if age >= 0 and age <= 4:
        print("Infants Free")
    elif age >= 5 and age <= 12:
        print("Children 10")
    elif age >= 13 and age <= 17:
        print("Adolescents 15")
    elif age >= 18 and age <= 64:
        print("Adults 20")
    elif age >= 65:
        print("Seniors 15")
    else:
        print("Invalid Age")

# Example usage:
# Read the age input from the user
age = int(input().strip())

# Call the function to categorize the visitor based on age
categorize_visitor(age)
