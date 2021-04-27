import math


if __name__ == '__main__':
    x = 234
    k = list(map(int, str(x)))
    x_prdt = math.prod(k)
    x_sum = sum(k)

    print(x_prdt - x_sum)