import re


def swap(odr):
    pattern = r'BG'
    x = re.sub(pattern, r'GB', odr)
    return x


if __name__ == '__main__':
    n, t = list(map(int, input().split()))
    order = input()


    for _ in range(t):
        order = swap(order)

    print(order)