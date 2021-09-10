def sort_recursion(ext_seq):
    '''Sorting Algorithm with recursion
    ext_seq: input !list with numbers
    :return: Ordered list
    '''
    # Copy the input list, because pop() will
    # change the original list
    sequence = ext_seq.copy()

    # Check if sequence is > 1 and numeric
    if len(sequence) <= 1:
        return sequence
    for s in sequence:
        if not str(s).isdigit():
            raise ValueError('sequence must be all numeric')

    # Initialize lists and first pivot number
    lower_number = []
    greater_number = []
    pivot = sequence.pop()

    # Compare every item in sequence with pivot
    for item in sequence:
        if item < pivot:
            lower_number.append(item)
        else:
            greater_number.append(item)

    # Run algorithm again and again, until
    # length sequence is <= 1
    return sort_recursion(lower_number) + [pivot] + sort_recursion(greater_number)


def sort_insertion(sequence):
    '''Sorting Algorithm with insertion
    sequence: input !list with numbers
    :return: Ordered list
    '''
    # Check if sequence is > 1 and numeric
    if len(sequence) <= 1:
        return sequence
    for s in sequence:
        if not str(s).isdigit():
            raise ValueError('sequence must be all numeric')

    length = range(0, len(sequence))
    # Insert every item in sequence and compare it
    # until it is bigger than i - 1
    for i in length:
        value = sequence[i]
        while sequence[i - 1] > value and i > 0:
            sequence[i], sequence[i - 1] = sequence[i - 1], sequence[i]
            i = i - 1
    return sequence


def l_number(sequence):
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


def h_number(sequence):
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
