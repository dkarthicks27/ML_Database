import re

if __name__ == '__main__':
    string = input()
    total = 0
    for i in range(len(string)):
        if string[i] == 'A':
            x = string.count('Q', 0, i)
            y = string.count('Q', i, len(string))
            total += x * y

    print(total)