def sortr(sequence):
    '''Sorting Algorithm with recursion
    sequence: input !list with numbers
    :return: Ordered list
    '''
    if len(sequence) <= 1:
        return sequence
    # Check if sequence is numeric
    for s in sequence:
        if not str(s).isdigit():
            raise ValueError('sequence must be all numeric')

    lower_number = []
    greater_number = []
    pivot = sequence.pop()

    for item in sequence:
        if item < pivot:
            lower_number.append(item)
        else:
            greater_number.append(item)
    return sortr(lower_number) + [pivot] + sortr(greater_number)


def sorti(sequence):
    '''Sorting Algorithm iterative
    sequence: input !list with numbers
    :return: Ordered list
    '''
    pass