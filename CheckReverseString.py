def is_reverse_string(str1, str2):
    """
    Check if str2 is the reverse of str1.
    
    Parameters:
    str1 (str): The first string.
    str2 (str): The second string.
    
    Returns:
    bool: True if str2 is the reverse of str1, False otherwise.
    """
    # Reverse str1 and check if it matches str2
    return str1[::-1] == str2