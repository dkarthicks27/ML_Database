if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, k = list(map(int, input().split()))
        arr = [i for i in range(1, n+1)]
        if n % 2 == 1:
            if n // 2 >= k:
                i = 0
                j = 1
                while i < k and j+1 < n:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    j += 2
                    i += 1
                    # now lets select 3 pairs at a time to shuffle

                print(' '.join(map(str, arr)))
            else:
                print(-1)

        else:
            if (n - 1)//2 >= k:
                i = 0
                j = 1
                while i < k and j + 1 < n:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    j += 2
                    i += 1
                    # now lets select 3 pairs at a time to shuffle

                print(' '.join(map(str, arr)))
            else:
                print(-1)