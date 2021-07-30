if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, k = list(map(int, input().split()))
        arr = list(map(int, input().split()))
        for i in range(n-1):
            if arr[i] < k:
                arr[n - 1] += arr[i]
                k -= arr[i]
                arr[i] = 0
            else:
                arr[i] -= k
                arr[n - 1] += k
                k = 0
                break

        print(' '.join(map(str, arr)))