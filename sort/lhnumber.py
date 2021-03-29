def lnumber(sequence):
    '''Find lowest number
    sequence: input !list with numbers
    :return: lowest number
    '''
    # Check if sequence is > 1 and numeric
    if len(sequence) <= 1:
        return sequence
    for s in sequence:
        if not str(s).isdigit():
            raise ValueError('sequence must be all numeric')

    # Initialize lowest_number with first list item
    lowest_number = sequence[0]

    # Compare every item in sequence with lowest_number
    # and replace it, if its lower
    for item in sequence:
        if item < lowest_number:
            lowest_number = item
    return lowest_number


def hnumber(sequence):
    '''Find highest number
    sequence: input !list with numbers
    :return: highest number
    '''
    # Check if sequence is > 1 and numeric
    if len(sequence) <= 1:
        return sequence
    for s in sequence:
        if not str(s).isdigit():
            raise ValueError('sequence must be all numeric')

    # Initialize highest_number with first list item
    highest_number = sequence[0]

    # Compare every item in sequence with highest_number
    # and replace it, if its higher
    for item in sequence:
        if item > highest_number:
            highest_number = item
    return highest_number
