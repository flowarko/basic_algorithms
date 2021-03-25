def sort_recursion(ext_seq):
    '''Sorting Algorithm with recursion
    ext_seq: input !list with numbers
    :return: Ordered list
    '''
    sequence = ext_seq.copy()
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
    return sort_recursion(lower_number) + [pivot] + sort_recursion(greater_number)


def sort_insertion(sequence):
    '''Sorting Algorithm with insertion
    sequence: input !list with numbers
    :return: Ordered list
    '''
    length = range(0, len(sequence))
    for i in length:
        value = sequence[i]

        while sequence[i-1] > value and i > 0:
            sequence[i], sequence[i-1] = sequence[i-1], sequence[i]
            i = i - 1
    return sequence
