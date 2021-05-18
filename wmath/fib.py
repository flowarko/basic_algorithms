def fibonacci(n):
    '''Fibonacci algorithm
    :param n: length of output list
    :return: list with fibonacci sequence
    '''
    out_lst = []
    a, b = 0, 1
    for i in range(n):
        out_lst.append(a)
        a, b = a + b, a

    return out_lst

