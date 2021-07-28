from sort.sort import *
from sort.lhnumber import *
from random import randint
from wmath.math import *
from icecream import ic

if __name__ == '__main__':
    # Testing Algorithms
    test_list = [randint(0, 100) for i in range(10)]
    test_number = randint(0, 20)
    test_number_celsius = randint(0, 40)
    print('Testlist: ' + str(test_list))
    print('Sort Recursion: ' + str(sort_recursion(test_list)))
    print('Sort Insertion: ' + str(sort_insertion(test_list)))
    print('Lowest Number: ' + str(lnumber(test_list)))
    print('Highest Number: ' + str(hnumber(test_list)))
    print('Prime Check of {}: {}'.format(test_number, prime_check(test_number)))
    print('Fibonacci of 10: {}'.format(fibonacci(test_number)))
    print('Faculty of {}: {}'.format(test_number, fak(test_number)))
    print('Converting {} Fahrenheit to Celsius: {}'.format(test_number, f_in_c(test_number)))
    print('Converting {} Celsius to Fahrenheit: {}'.format(test_number_celsius, c_in_f(test_number_celsius)))
    print('')
    # Testing icecream for debugging
    ic(sort_recursion(test_list))
    ic(sort_insertion(test_list))
    ic(lnumber(test_list))
    ic(hnumber(test_list))
    ic(prime_check(test_number))
    ic(fibonacci(test_number))
    ic(fak(test_number))
    ic(f_in_c(test_number))
    ic(c_in_f(test_number_celsius))
