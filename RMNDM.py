from os import *
from sys import *
from collections import *
from math import *

def rotateMatrix(matrix):
    n = len(matrix)  # Get the size of the matrix (n x n)

    # Transpose the matrix: swap elements across the diagonal
    for i in range(n):
        for j in range(i, n):
            # Swap element at (i, j) with element at (j, i)
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Reverse each column to achieve a 90-degree anti-clockwise rotation
    for j in range(n):
        for i in range(n // 2):
            # Swap elements in the column: top with bottom
            matrix[i][j], matrix[n - i - 1][j] = matrix[n - i - 1][j], matrix[i][j]

    return matrix  # Return the rotated matrix