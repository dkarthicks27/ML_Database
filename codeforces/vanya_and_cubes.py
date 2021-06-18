import math

if __name__ == '__main__':
    n = int(input())
    if n == 1:
        print(1)
    else:
        i = math.floor((n * 6) ** (1 / 3))
        if i * (i + 1) * (i + 2) <= n * 6:
            print(i)
        elif (i - 1) * i * (i + 1) <= n * 6:
            print(i - 1)
        else:
            print(i + 1)

