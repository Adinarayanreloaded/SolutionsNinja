from os import *
from sys import *
from collections import *
from math import *

def stringSum(num1: str, num2: str) -> str:
    # Initialize pointers, carry, and result list
    i, j = len(num1) - 1, len(num2) - 1
    carry = 0
    result = []
    
    # Iterate while there are digits to process or there's a carry
    while i >= 0 or j >= 0 or carry:
        # Get the digits at current positions or 0 if out of bounds
        x = int(num1[i]) if i >= 0 else 0
        y = int(num2[j]) if j >= 0 else 0
        
        # Calculate the sum of digits and carry
        total = x + y + carry
        carry = total // 10  # Calculate carry for the next position
        result.append(total % 10)  # Add the last digit of the sum to the result
    
        # Move to the next digits
        i -= 1
        j -= 1
    
    # Convert result to string and reverse it
    return ''.join(map(str, result[::-1]))
