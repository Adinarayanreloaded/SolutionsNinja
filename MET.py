def Multiply(test_tup):
    # Initialize the product variable to 1 (the multiplicative identity)
    product = 1
    
    # Iterate over each element in the tuple
    for num in test_tup:
        # Multiply the current product by the element
        product *= num
    
    # Return the final product
    return product
