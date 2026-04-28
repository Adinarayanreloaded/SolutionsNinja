from typing import List

def printRowWise(a: List[List[int]]) -> List[int]:
    """
    Traverses the matrix row-wise and returns a list of elements in the order of traversal.
    
    Parameters:
    a (List[List[int]]): The matrix to be traversed.
    
    Returns:
    List[int]: A list of elements traversed row-wise.
    """
    # Initialize an empty list to store the row-wise traversal
    result = []
    
    # Traverse each row in the matrix
    for row in a:
        # Append all elements of the current row to the result list
        result.extend(row)
    
    return result

