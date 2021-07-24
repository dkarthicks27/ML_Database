from collections import Counter

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        c = Counter(arr)
        res = list(sorted(set(c.keys())))
        final = []
        for i in res:
            if c[i] > 1:
                final.extend([i for j in range(c[i] - 1)])
        res.extend(final)
        print(' '.join(map(str, res)))
