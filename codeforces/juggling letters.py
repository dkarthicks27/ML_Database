from collections import Counter


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        # get the length of the strings
        n = int(input())
        x = None
        for i in range(n):
            if i == 0:
                x = Counter(input())
            else:
                x.update(input())

        stay = True
        for keys in x.keys():
            if x[keys] % n != 0:
                stay = False
                break

        if stay:
            print('YES')
        else:
            print('NO')