from collections import Counter


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        if len(set(arr)) == 1:
            print(0)
        else:
            weakest = min(arr)
            res = Counter(arr)
            total = 0
            for i in res.keys():
                if i != weakest:
                    total += res[i]

            print(total)