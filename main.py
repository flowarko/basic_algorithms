from sort.sort import *
from sort.lhnumber import *
from wmath.prime import prime_check
from wmath.fib import fibonacci
from random import randint
from wmath.temperatures import *

if __name__ == '__main__':
    # Testing Algorithms
    test_list = [randint(0, 100) for i in range(10)]
    test_number = randint(0, 100)
    test_number_celsius = randint(0, 40)
    print('Testlist: ' + str(test_list))
    print('Sort Recursion: ' + str(sort_recursion(test_list)))
    print('Sort Insertion: ' + str(sort_insertion(test_list)))
    print('Lowest Number: ' + str(lnumber(test_list)))
    print('Highest Number: ' + str(hnumber(test_list)))
    print('Prime Check of {}: {}'.format(test_number, prime_check(test_number)))
    print('Fibonacci of 10: {}'.format(fibonacci(10)))
    print('Converting {} Fahrenheit to Celsius: {}'.format(test_number, f_in_c(test_number)))
    print('Converting {} Celsius to Fahrenheit: {}'.format(test_number_celsius, c_in_f(test_number_celsius)))
