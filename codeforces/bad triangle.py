if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        arr.sort()
        if arr[0] + arr[1] <= arr[n - 1]:
            print(1, 2, n)
        else:
            print(-1)
