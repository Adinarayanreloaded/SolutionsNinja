def reverseEachWord(string):
    # Split the sentence into words
    words = string.split()
    
    # Reverse each word
    reversed_words = [word[::-1] for word in words]
    
    # Join the reversed words into a single string
    reversed_sentence = ' '.join(reversed_words)
    
    return reversed_sentence