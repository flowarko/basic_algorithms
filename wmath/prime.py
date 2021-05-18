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