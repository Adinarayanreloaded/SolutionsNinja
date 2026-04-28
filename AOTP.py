def findSubstringIndices(string, pattern):
    """
    Finds all starting indices of occurrences of the pattern in the string.

    Parameters:
    string (str): The string in which to search for occurrences of the pattern.
    pattern (str): The pattern to search for in the string.

    Returns:
    List[int]: A list of starting indices where the pattern is found in the string.
    """
    # List to store the starting indices of occurrences of the pattern
    indices = []
    
    # Length of the pattern
    pattern_length = len(pattern)
    
    # Iterate over the string to check for occurrences of the pattern
    for i in range(len(string) - pattern_length + 1):
        # Check if the substring starting at index i matches the pattern
        if string[i:i + pattern_length] == pattern:
            indices.append(i)
    
    # Return the list of starting indices
    return indices

