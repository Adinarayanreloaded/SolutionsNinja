def find_unique_element(arr):
    # Create a dictionary to store the frequency of each element
    frequency = {}
    
    # Populate the dictionary with element counts
    for num in arr:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    
    # Find and return the unique element (frequency of 1)
    for num, count in frequency.items():
        if count == 1:
            return num
    
    # Return None if no unique element is found
    return None