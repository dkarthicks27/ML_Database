import re


if __name__ == '__main__':
    inp = input()
    inp2 = input()
    pattern = ''
    for i in inp:
        pattern = pattern + i + r'{1,}'

    print(bool(re.search(pattern, inp2)))
