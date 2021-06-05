import re

"""
so given a string inp and a number no, we need to find and remove all consecutive same elements whose count is
exactly equal to no

For eg:
inp = 'aabccd'
no = 2

then output:
out = 'bd'

reason:
so as you observe both "c" and "a" have a count of 2 so we have removed it

"""

if __name__ == '__main__':
    inp, no = input().split()
    no = int(no)


    pattern = rf'(\w){{{no}}}'

    z = re.finditer(pattern, inp)
    for mt in z:
        new_str = mt.group()
        inp = inp.replace(new_str, '')

    print(inp)

