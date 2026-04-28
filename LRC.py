from sys import stdin
from typing import List, Tuple

from typing import List, Tuple

def findLargestSum(mat: List[List[int]], n: int, m: int) -> Tuple[str, int, int]:
    
    # Edge case for an empty matrix
    if n == 0 or m == 0:
        # If there are no rows or columns, return default values
        return ("row", 0, -2147483648)  # Smallest integer value used to handle edge case
    
    # Initialize variables for tracking the maximum sum and the corresponding row/column
    max_sum = float('-inf')  # Set initial max_sum to the smallest possible value
    result_type = ""  # Will store whether the maximum sum is from a "row" or "column"
    result_index = -1  # Will store the index of the row or column with the maximum sum
    
    # Iterate over each row to find the maximum row sum
    for i in range(n):
        row_sum = sum(mat[i])  # Calculate the sum of elements in the ith row
        if row_sum > max_sum:  # Check if this row's sum is greater than the current max_sum
            max_sum = row_sum  # Update max_sum to this new maximum sum
            result_type = "row"  # Set the result type to "row"
            result_index = i  # Update the result index to the current row index
    
    # Iterate over each column to find the maximum column sum
    for j in range(m):
        # Calculate the sum of elements in the jth column
        col_sum = sum(mat[i][j] for i in range(n))  
        if col_sum > max_sum:  # Check if this column's sum is greater than the current max_sum
            max_sum = col_sum  # Update max_sum to this new maximum sum
            result_type = "column"  # Set the result type to "column"
            result_index = j  # Update the result index to the current column index
    
    # Return the type of the maximum sum ("row" or "column"), the index of the row/column, and the maximum sum value
    return (result_type, result_index, max_sum)


def take2DInput() -> Tuple[List[List[int]], int, int]:
    n, m = map(int, stdin.readline().strip().split())
    mat = []
    for _ in range(n):
        row = list(map(int, stdin.readline().strip().split()))
        mat.append(row)
    return mat, n, m

# Main
t = int(stdin.readline().rstrip())

while t > 0:
    mat, nRows, mCols = take2DInput()
    result_type, result_index, max_sum = findLargestSum(mat, nRows, mCols)
    print(result_type, result_index, max_sum)
    t -= 1
