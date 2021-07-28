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

def fak(n):
    '''Faculty algorithm
    :param n: faculty of n numbers
    :return: 1*2*3*n
    '''
    if n < 1:
        return

    e = 1
    for i in range(n):
        e = e * (i+1)

    return e


def prime_check(number):
    '''Check if number is wmath
    number: input number
    :return: True (wmath)
             False (not a wmath)
    '''
    # Check if sequence is > 1 and numeric
    if not str(number).isdigit():
        raise ValueError('number must be a number')

    # Try every number smaller than number with
    # modulo. If number modulo i 0, it's not a wmath
    for i in range(1, number):
        if number % i == 0 and i != 1:
            return False
    return True

def f_in_c(value):
    ''' Convert Fahrenheit to Celsius
    :param value: Input Fahrenheit
    :return: Output Celsius
    '''
    return (value - 32) / 1.8


def c_in_f(value):
    ''' Convert Celsius to Fahrenheit
    :param value: Input Celsius
    :return: Output Fahrenheit
    '''
    return value * 1.8 + 32
