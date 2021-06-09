import math

if __name__ == '__main__':
    n, k = list(map(int, input().split()))

    rem_time = 240 - k  # mins available at last
    p = 2 * rem_time / 5
    max_n = math.floor(math.sqrt((2 * rem_time / 5)))
    if max_n * (max_n + 1) > p:
        max_n -= 1
    if max_n > n:
        print(n)
    else:
        print(max_n)