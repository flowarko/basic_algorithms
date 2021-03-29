from sort.sort import *
from sort.lhnumber import *
from prime.check import *
from random import randint

if __name__ == '__main__':
    # Testing Algorithms
    test_list = [randint(0, 100) for i in range(10)]
    test_number = randint(0, 100)
    print('Testlist: ' + str(test_list))
    print('Sort Recursion: ' + str(sort_recursion(test_list)))
    print('Sort Insertion: ' + str(sort_insertion(test_list)))
    print('Lowest Number: ' + str(lnumber(test_list)))
    print('Highest Number: ' + str(hnumber(test_list)))
    print('Prime Check of {}: {}'.format(test_number, prime_check(test_number)))
