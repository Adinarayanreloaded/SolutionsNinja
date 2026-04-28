from os import *
from sys import *
from collections import *
from math import *

def findTargetInMatrix(mat, m, n, target):
    """
    Function to find if the target exists in the given matrix.

    Parameters:
    mat (List[List[int]]): 2D matrix with sorted rows and increasing order of first elements of each row.
    m (int): Number of rows in the matrix.
    n (int): Number of columns in the matrix.
    target (int): The value to be searched in the matrix.

    Returns:
    bool: True if target is found, False otherwise.
    """
    
    # Define the initial boundaries for binary search in a 1D view of the 2D matrix
    start, end = 0, m * n - 1

    while start <= end:
        # Calculate the middle index of the current search range
        mid = start + (end - start) // 2
        
        # Convert the middle index to 2D matrix coordinates
        val = mat[mid // n][mid % n]
        
        # If the target is less than the middle value, search the left half
        if target < val:
            end = mid - 1
        # If the target is greater than the middle value, search the right half
        elif target > val:
            start = mid + 1
        # If the target matches the middle value, return True
        else:
            return True
    
    # If the loop ends, the target is not found in the matrix
    return False
