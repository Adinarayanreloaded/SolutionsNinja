import sys
from copy import deepcopy
from sys import stdin, setrecursionlimit
from typing import List
setrecursionlimit(10**7)

def transpose(m: int, n: int, mat: List[List[int]]) -> List[List[int]]:
    # Initialize the transposed matrix with dimensions n x m
    transposed = [[0] * m for _ in range(n)]
    
    # Iterate through the original matrix and fill the transposed matrix
    for i in range(m):
        for j in range(n):
            transposed[j][i] = mat[i][j]
    
    return transposed

class Runner:
    def __init__(self):
        self.t = 0
        self.n = []
        self.m = []
        self.matrix = []

    # Fast input
    def takeInput(self):
        input = sys.stdin.read().split()
        index = 0
        self.t = int(input[index])
        index += 1

        for i in range(self.t):
            m = int(input[index])
            n = int(input[index + 1])
            index += 2
            self.m.append(m)
            self.n.append(n)

            matrix = []
            for _ in range(m):
                row = list(map(int, input[index:index + n]))
                index += n
                matrix.append(row)
            self.matrix.append(matrix)

    def executeAndPrintOutput(self):
        for i in range(self.t):
            ans = transpose(self.m[i], self.n[i], self.matrix[i])
            for row in ans:
                print(" ".join(map(str, row)))

if __name__ == "__main__":
    runner = Runner()
    runner.takeInput()
    runner.executeAndPrintOutput()

