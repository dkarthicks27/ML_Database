if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        if n < 10:
            print(n)
        else:
            count = 0
            for i in range(10, n+1):
                k = set([p for p in str(i)])
                if len(k) == 1:
                    count += 1
            print(count+9)