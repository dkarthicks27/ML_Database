if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        prod = 1
        for i in range(n-1):
            prod = max(prod, arr[i] * arr[i + 1])

        print(prod)