if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        tot = sum(arr)
        if tot / n == 1:
            print(0)
        else:
            if tot > 0:
                if tot > n:
                    print(tot - n)
                else:
                    print(1)
            else:
                print(1)