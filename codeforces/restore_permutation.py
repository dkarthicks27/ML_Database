if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        p = set()
        li = list(map(int, input().split()))
        new_list = []
        for i in li:
            if i not in p:
                p.add(i)
                new_list.append(i)
        print(' '.join([str(x) for x in new_list]))
