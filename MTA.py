def Merge(arr1, arr2):
    # Convert both lists to sets to remove duplicates and then merge them
    merged_set = set(arr1) | set(arr2)
    
    # Convert the set back to a list and sort it
    merged_list = sorted(merged_set)
    
    # Return the merged list
    return merged_list
