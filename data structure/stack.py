import math
import os
import random
import re
import sys


#
# Complete the 'getMax' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY operations as parameter.
#
class Stack:
    def __init__(self):
        self.stack = []

    def insert_ele(self, x):
        if not self.stack:
            self.stack.append(x)
        else:
            self.stack.append(max(x, self.stack[-1]))

    def remove_ele(self):
        if self.stack:
            self.stack.pop()

    def find_max(self):
        return self.stack[-1]



def getMax(operations):
    arr = []
    st = Stack()
    for op in operations:
        if len(op.split(' ')) == 2:
            # it is type 1 command
            command, val = list(map(int, op.split(' ')))
            st.insert_ele(val)
        elif int(op) == 2:
            st.remove_ele()
        else:
            arr.append(st.find_max())

    return arr


if __name__ == '__main__':
    n = int(input().strip())

    ops = []

    for _ in range(n):
        ops_item = input()
        ops.append(ops_item)

    res = getMax(ops)
    print(res)