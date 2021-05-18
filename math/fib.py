def fibonacci(n):
    '''
    Fibonacci
    :param n: how many times to add
    :return: list with fibonacci sequence
    '''
    out_lst = []
    a, b = 0, 1
    for i in range(n):
        out_lst.add(a)
        a, b = a + b, a

    return out_lst

