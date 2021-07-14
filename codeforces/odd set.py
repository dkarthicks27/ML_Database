if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        even = 0
        odd = 0
        for i in arr:
            if i % 2 == 0:
                even += 1
            else:
                odd += 1

        if even == odd:
            print('YES')
        else:
            print('NO')
