def maxfreq(arr):
    if not arr:
        return None

    frequency = {}
    first_occurrence = {}

    # Fill the dictionaries
    for index, num in enumerate(arr):
        if num not in frequency:
            frequency[num] = 0
            first_occurrence[num] = index
        frequency[num] += 1

    # Find the number with maximum frequency
    max_freq = 0
    result = None

    for num in frequency:
        if frequency[num] > max_freq or (frequency[num] == max_freq and first_occurrence[num] < first_occurrence[result]):
            max_freq = frequency[num]
            result = num

    return result
