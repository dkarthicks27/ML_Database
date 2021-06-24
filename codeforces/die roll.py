from math import gcd

def reduce_fractions(a, b):
    d = gcd(a, b)
    a = a // d
    b = b // d
    return a, b


if __name__ == '__main__':
    # so the possible values for a six sided die are 1, 2, 3, 4, 5, 6
    yak, wak = list(map(int, input().split()))
    possible_values = list(range(max(yak, wak), 7))
    x = len(possible_values)
    y = 6

    x, y = reduce_fractions(x, y)
    print(f'{x}/{y}')
