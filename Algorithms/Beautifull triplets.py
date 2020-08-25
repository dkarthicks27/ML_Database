#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


# Complete the beautifulTriplets function below.
def beautifulTriplets(d, arr):
    dictionary = Counter(arr)
    tripletCount = 0
    for element in dictionary.keys():
        element1 = element
        # I am going to check if there is a second and third element of our
        # triplet present, if this is there then I going to calculate
        # the total combinations in which these can be used
        element2 = element1 + d
        element3 = element1 + 2 * d

        # these are the two conditions which need to be satisfied for it to be triplet
        condition1 = dictionary.get(element1 + d)
        condition2 = dictionary.get(element1 + 2 * d)
        if condition1 is not None and condition2 is not None:
            tripletCount += dictionary[element1] * dictionary[element2] * dictionary[element3]

    return tripletCount


if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    arr = list(map(int, input().rstrip().split()))
    result = beautifulTriplets(d, arr)
    print(result)

