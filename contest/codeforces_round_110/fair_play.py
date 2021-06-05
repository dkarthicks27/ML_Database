def solve(array):
    x = sorted(array)
    max1 = x[-1]
    max2 = x[-2]

    finalist = [max(array[0], array[1]), max(array[2], array[3])]
    if max1 in finalist and max2 in finalist:
        print('YES')
    else:
        print('NO')







if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        matches = list(map(int, input().split()))
        solve(matches)