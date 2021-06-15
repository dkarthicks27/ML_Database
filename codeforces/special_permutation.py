if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        n = int(input())
        li = list(range(1, n+1))
        if len(li) % 2 == 0:
            li.reverse()
            print(' '.join(str(i) for i in li))
        else:
            mid = (len(li) + 1) // 2 - 1
            li.reverse()
            temp = li[mid]
            li[mid] = li[mid + 1]
            li[mid + 1] = temp

            print(' '.join(str(i) for i in li))
