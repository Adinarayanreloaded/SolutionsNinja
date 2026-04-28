from os import *
from sys import *
from collections import *
from math import *

def matrixBoundaryTraversal(MAT, M, N):
    boundary_elements = []

    # Top row
    for j in range(N):
        boundary_elements.append(MAT[0][j])
    
    # Bottom row
    if M > 1:
        for j in range(N):
            boundary_elements.append(MAT[M-1][j])
    
    # Left column (excluding corners if M > 1)
    for i in range(1, M-1):
        boundary_elements.append(MAT[i][0])
    
    # Right column (excluding corners if M > 1)
    if N > 1:
        for i in range(1, M-1):
            boundary_elements.append(MAT[i][N-1])
    
    return boundary_elements

