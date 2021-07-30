if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        size_n = 2 * n
        arr = list(map(int, input().split()))
        arr.sort()
        arr1 = arr[:n]
        arr2 = arr[n:]
        i = 0
        p = 0
        q = 0
        for i in range(size_n):
            if i % 2 == 0:
                print(arr2[p], sep=" ", end=" ")
                p += 1
            else:
                print(arr1[q], sep=" ", end=" ")
                q += 1
        print("")