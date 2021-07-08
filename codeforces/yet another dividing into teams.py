if __name__ == '__main__':
    q = int(input())
    for _ in range(q):
        n = int(input())
        arr = list(map(int, input().split()))
        if n == 1:
            print(1)
        else:
            arr.sort()
            res = 0
            for i in range(n-1):
                if arr[i+1] - arr[i] == 1:
                    res = 1
                    break

            if res:
                print(2)
            else:
                print(1)