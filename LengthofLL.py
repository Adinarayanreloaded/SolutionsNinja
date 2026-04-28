def length(head):
    """
    Function to calculate the length of a linked list.
    
    :param head: The head node of the linked list.
    :return: The length of the linked list.
    """
    count = 0  # Initialize the count to 0
    
    # Traverse the linked list
    current = head  # Start with the head node
    while current is not None:  # While there are more nodes to traverse
        count += 1  # Increment the count for each node
        current = current.next  # Move to the next node
    
    return count  # Return the total number of nodes in the list
