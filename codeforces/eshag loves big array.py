if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        if len(set(arr)) == 1:
            print(0)
        else:
            x = arr.count(min(arr))
            print(n - x)
