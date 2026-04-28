# Define a custom exception for insufficient funds
class InsufficientFundsException(Exception):
    def __init__(self, message="Insufficient funds in the account."):
        self.message = message
        super(InsufficientFundsException, self).__init__(self.message)

# Define the BankAccount class
class BankAccount:
    def __init__(self):
        self.balance = 500  # Initial balance set to 500

    def withdraw(self, amount):
        if amount > self.balance:
            # Raise the custom exception if withdrawal amount is greater than the balance
            raise InsufficientFundsException()
        else:
            # Calculate the remaining balance after withdrawal
            remaining_balance = self.balance - amount
            # Update the balance
            self.balance = remaining_balance
            # Output the remaining balance
            print("Remaining:{}".format(remaining_balance))

# Main function to handle user input and call the withdraw method
if __name__ == "__main__":
    account = BankAccount()
    
    # Read input from the user
    amount = int(input().strip())
    
    try:
        account.withdraw(amount)
    except InsufficientFundsException as e:
        print(e)
# Define a custom exception for insufficient funds
class InsufficientFundsException(Exception):
    def __init__(self, message="Insufficient funds in the account."):
        self.message = message
        super(InsufficientFundsException, self).__init__(self.message)

# Define the BankAccount class
class BankAccount:
    def __init__(self):
        self.balance = 500  # Initial balance set to 500

    def withdraw(self, amount):
        if amount > self.balance:
            # Raise the custom exception if withdrawal amount is greater than the balance
            raise InsufficientFundsException()
        else:
            # Calculate the remaining balance after withdrawal
            remaining_balance = self.balance - amount
            # Update the balance
            self.balance = remaining_balance
            # Output the remaining balance
            print("Remaining:{}".format(remaining_balance))

# Main function to handle user input and call the withdraw method
if __name__ == "__main__":
    account = BankAccount()
    
    # Read input from the user
    amount = int(input().strip())
    
    try:
        account.withdraw(amount)
    except InsufficientFundsException as e:
        print(e)
