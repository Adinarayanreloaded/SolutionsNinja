def checkArmstrong(n):
    # Convert the number to a string to easily iterate over digits
    digits = str(n)
    # Count the number of digits
    k = len(digits)
    # Compute the sum of each digit raised to the power of k
    armstrong_sum = sum(int(digit) ** k for digit in digits)
    # Check if the computed sum is equal to the original number
    return armstrong_sum == n

