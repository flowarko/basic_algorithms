def lnumber(sequence):
    '''Find lowest number
    sequence: input !list with numbers
    :return: lowest number
    '''
    if len(sequence) <= 1:
        return sequence
    # Check if sequence is numeric
    for s in sequence:
        if not str(s).isdigit():
            raise ValueError('sequence must be all numeric')

    lowest_number = sequence[0]

    for item in sequence:
        if item < lowest_number:
            lowest_number = item
    return lowest_number

def hnumber(sequence):
    '''Find highest number
    sequence: input !list with numbers
    :return: highest number
    '''
    if len(sequence) <= 1:
        return sequence
    # Check if sequence is numeric
    for s in sequence:
        if not str(s).isdigit():
            raise ValueError('sequence must be all numeric')

    highest_number = sequence[0]

    for item in sequence:
        if item > highest_number:
            highest_number = item
    return highest_number