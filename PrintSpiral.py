from typing import List
import sys
input = sys.stdin.read  # Use sys.stdin.read to take entire input at once

def spiralOrder(matrix: List[List[int]]) -> List[int]:
    if not matrix or not matrix[0]:
        return []

    result = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:
        # Traverse from left to right along the top row
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1

        # Traverse from top to bottom along the right column
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1

        if top <= bottom:
            # Traverse from right to left along the bottom row
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1

        if left <= right:
            # Traverse from bottom to top along the left column
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1

    return result

def take2DInput():
    data = input().strip().split("\n")
    t = int(data[0])
    index = 1
    
    results = []
    
    for _ in range(t):
        nRows, mCols = map(int, data[index].split())
        index += 1
        
        if nRows == 0:
            results.append([])
            continue
        
        mat = []
        for _ in range(nRows):
            mat.append(list(map(int, data[index].split())))
            index += 1
        
        spiral_order = spiralOrder(mat)
        results.append(spiral_order)
    
    return results

def main():
    results = take2DInput()
    for result in results:
        print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()
