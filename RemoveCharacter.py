def remove_all_occurrences_of_char(input_string, char_to_remove):
    """
    Removes all occurrences of the specified character from the input string.

    Parameters:
    input_string (str): The string from which characters will be removed.
    char_to_remove (str): The character that will be removed from the string.

    Returns:
    str: A new string with all occurrences of char_to_remove removed.
    """
    # Initialize an empty list to store characters that are not `char_to_remove`
    result = []

    # Iterate through each character in the `input_string`
    for char in input_string:
        # If the current character is not `char_to_remove`, append it to the result list
        if char != char_to_remove:
            result.append(char)

    # Join the list into a single string and return it
    print(''.join(result))
