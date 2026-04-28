from typing import *

def printColWise(a: List[List[int]]) -> List[int]:
    """
    Traverses the matrix column-wise and returns a list of elements in the order of traversal.
    
    Parameters:
    a (List[List[int]]): The matrix to be traversed.
    
    Returns:
    List[int]: A list of elements traversed column-wise.
    """
    # Initialize an empty list to store the column-wise traversal
    result = []
    
    # Number of rows (N) and columns (M) in the matrix
    N = len(a)
    M = len(a[0]) if N > 0 else 0
    
    # Traverse each column
    for j in range(M):
        for i in range(N):
            # Append the element at position (i, j) to the result list
            result.append(a[i][j])
    
    return result