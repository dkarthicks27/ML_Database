"""Algorithm: 1011010
So it is actually left rotation

So what we can actually do is that we can probably shift each time convert to decimal and see if there exist a integer log for this number but I don’t know if this method is feasible


Take the input string save it to a variable original

1. Convert it to decimal and then check if there exist a positive log to the base 2 for this number
2. If it exist, store it as current value and also check if its greater than previous value if its replace it as the new value
3. Now check left shift the string and check if it is different from the original, if its different repeat the process else exist.
"""
from math import log2
from copy import deepcopy


def leftShift(string):
    new_string = string[-1] + string[:-1]
    return new_string


def maximumPower(string):
    originals = deepcopy(string)
    print('string: ', string)
    original = string
    number = int(original, 2)
    print('number:', number)
    val = log2(number)
    print('val: ', val)
    maximumVal = 0
    if val.is_integer():
        maximumVal = int(val)
        string = leftShift(originals)
        while string != originals:
            print('\n')
            print('binary string:', string)
            number = int(string, 2)
            print('decimal value:', number)
            val = log2(number)
            print('val:', val)
            if val.is_integer():
                maximumVal = max(maximumVal, int(val))
            print('maximum_value: ', maximumVal)
            string = leftShift(string)
    else:
        string = leftShift(originals)
        while string != originals:
            print('\n')
            print('binary string:', string)
            number = int(string, 2)
            print('decimal value:', number)
            val = log2(number)
            print('val:', val)
            if val.is_integer():
                maximumVal = max(maximumVal, int(val))
            print('maximum_value: ', maximumVal)
            string = leftShift(string)


    print('\n\n\n')
    return maximumVal


print(maximumPower('0011'))


