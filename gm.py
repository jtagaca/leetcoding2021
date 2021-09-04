import sys
# import numpy as np
# import pandas as pd
# from sklearn import ...


def powerofTwo(line):
    number = int(line)

    # edge case in case it is 0
    if number == 0:
        return False
    # we keep going till we check to see if this is not odd
    # then we know it is not a power of 2
    while number > 1:
        if number % 2 != 0:
            return False
        number = number//2
    return True


for line in sys.stdin:
    powerofTwo(line)
    # print(line)
    # compareNum(line)
