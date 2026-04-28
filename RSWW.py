def reverseStringWordWise(string):
    # Step 1: Split the string into words
    words = string.split()
    
    # Step 2: Reverse the list of words
    reversed_words = words[::-1]
    
    # Step 3: Join the reversed list into a single string
    result = ' '.join(reversed_words)
    
    return result