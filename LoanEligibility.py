# Read inputs for age, monthly income, and outstanding loans
age = int(input().strip())
monthly_income = float(input().strip())
has_loans = input().strip().lower() == 'true'

# Check eligibility criteria
if age >= 18 and monthly_income >= 2000 and not has_loans:
    print("You are eligible for the loan.")
else:
    print("You are not eligible for the loan.")
