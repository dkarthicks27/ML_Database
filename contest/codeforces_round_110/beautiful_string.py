import re

if __name__ == '__main__':
    string = '0?10'

    pattern = r'(01){1,}|(10){1,}'
    x = re.match(pattern, string)

    print(x)