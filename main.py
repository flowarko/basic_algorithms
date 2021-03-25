from sort.sort import *
from sort.lhnumber import *
from random import randint

if __name__ == '__main__':
    # Testing Algorithms
    print(sortr([randint(0, 100) for i in range(10)]))
    print(lnumber([randint(0, 100) for i in range(10)]))
    print(hnumber([randint(0, 100) for i in range(10)]))