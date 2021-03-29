from sort.sort import *
from sort.lhnumber import *
from random import randint

if __name__ == '__main__':
    # Testing Algorithms
    test_list = [randint(0, 100) for i in range(10)]
    print('Testlist: ' + str(test_list))
    print(sort_recursion(test_list))
    print(sort_insertion(test_list))
    print(lnumber(test_list))
    print(hnumber(test_list))
