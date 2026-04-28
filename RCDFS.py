def removeConsecutiveDuplicates(string):
    i = 0 
    j = 0
    new_elements = ''
     
    # Iterate through the string using the j pointer.
    while j < len(string):
         
        # If both elements are the same, skip the current element.
        if string[i] == string[j]:
            j += 1
             
        # If the elements are not the same, append the current character.
        else:
            new_elements += string[i]
            # Move the i pointer to the current j position.
            i = j
    
    # Append the last character after the loop ends.
    new_elements += string[j-1]
    
    return new_elements

