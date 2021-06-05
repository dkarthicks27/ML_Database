import math


def solve(arr):
    count = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if math.gcd(arr[i], 2 * arr[j]) > 1:
                count += 1

    print(count)
    pass


if __name__ == '__main__':
    # t = int(input())
    # for _ in range(t):
    #     n = input()
    #     array = list(map(int, input().split()))
    array = [4, 4, 2, 1, 1]
    solve(array)
