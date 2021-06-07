import math

def odd_part(n):
    return (n / 2) * (-1 - (n * 2 - 1))

def even_part(n):
    return (n / 2) * (2 + n * 2)


if __name__ == '__main__':
    n = int(input())

    if n % 2 == 0:
        print(n // 2)

    else:
        print(-n + (n - 1)//2)
