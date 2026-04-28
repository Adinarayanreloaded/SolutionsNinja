from math import *
from collections import *
from sys import *

from typing import List

def setZeros(matrix: List[List[int]]) -> None:
    """
    Sets entire rows and columns to 0 if any element in that row or column is 0.
    This function modifies the matrix in place.
    
    Parameters:
    matrix (List[List[int]]): 2D list of integers where zeros will be set in rows and columns.
    """
    if not matrix or not matrix[0]:
        return
    
    nRows = len(matrix)
    mCols = len(matrix[0])
    
    # Create boolean lists to track which rows and columns need to be zeroed
    zero_rows = [False] * nRows
    zero_cols = [False] * mCols
    
    # First pass: identify rows and columns that need to be zeroed
    for i in range(nRows):
        for j in range(mCols):
            if matrix[i][j] == 0:
                zero_rows[i] = True
                zero_cols[j] = True
    
    # Second pass: zero out the rows
    for i in range(nRows):
        if zero_rows[i]:
            for j in range(mCols):
                matrix[i][j] = 0
    
    # Third pass: zero out the columns
    for j in range(mCols):
        if zero_cols[j]:
            for i in range(nRows):
                matrix[i][j] = 0