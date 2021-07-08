from collections import Counter

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        ans = Counter(arr)
        least = n + 1
        for key, value in ans.items():
            if value == 1:
                least = min(least, key)

        if least == n + 1:
            print(-1)
        else:
            print(arr.index(least)+1)