from sys import stdin

def rowWiseSum(mat, nRows, mCols):
    
    # Create an empty list to store the sum of each row
    row_sums = []

    # Iterate through each row in the matrix
    for i in range(nRows):
        # Compute the sum of the current row
        row_sum = sum(mat[i])
        print(row_sum, end = ' ')
        # Append the row sum to the list of row sums
        row_sums.append(row_sum)

    # Convert the list of row sums to a string where each sum is separated by a space
    return ' '.join(map(str, row_sums))


#Taking Input Using Fast I/O
def take2DInput() :
    li = stdin.readline().rstrip().split(" ")
    nRows = int(li[0])
    mCols = int(li[1])
    
    if nRows == 0 :
        return list(), 0, 0
    
    mat = [list(map(int, input().strip().split(" "))) for row in range(nRows)]
    return mat, nRows, mCols


#main
t = int(stdin.readline().rstrip())

while t > 0 :

    mat, nRows, mCols = take2DInput()
    rowWiseSum(mat, nRows, mCols)
    print()

    t -= 1