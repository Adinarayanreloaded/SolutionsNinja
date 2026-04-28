def find_max_min(data):
    # Initialize the result list to store max and min values
    result = []
    
    # Find the maximum and minimum elements in the data
    max_element = max(data)
    min_element = min(data)
    
    # Append the max and min elements to the result list
    result.append(max_element)
    result.append(min_element)
    
    # Return the result as a tuple
    return tuple(result)