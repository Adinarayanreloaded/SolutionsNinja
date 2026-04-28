def anagramPairs(n: int, m: int, s: str, t: str) -> bool:
    # Check if the lengths of the strings are the same
    if n != m:
        return False
    
    # Create frequency dictionaries for both strings
    freq_s = {}
    freq_t = {}
    
    for char in s:
        freq_s[char] = freq_s.get(char, 0) + 1
    
    for char in t:
        freq_t[char] = freq_t.get(char, 0) + 1
    
    # Compare the frequency dictionaries
    return freq_s == freq_t