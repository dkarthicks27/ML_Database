if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        n = int(input())
        li = list(map(int, input().split()))
        ele = set(li)
        for i in ele:
            if li.count(i) == 1:
                print(li.index(i) + 1)