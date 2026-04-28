# Constant for the late fee per day
LATE_FEE_PER_DAY = 0.25

# Ask the user to input the number of days late
days_late = int(input())

# Calculate the total fee
total_fee = days_late * LATE_FEE_PER_DAY

# Print the total amount owed
print(total_fee)
