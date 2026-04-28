def StartingIndex(data, target):
    # Iterate through the list
    for index in range(len(data)):
        # Check if the current element is the target
        if data[index] == target:
            return index
    # If the target is not found, return -1
    return -1
