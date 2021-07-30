if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        check = set()
        count = 0
        for i in arr:
            if i not in check:
                check.add(i)
                count += 1
            else:
                if i + 1 not in check:
                    check.add(i + 1)
                    count += 1

        print(count)