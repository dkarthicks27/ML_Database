if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    stored_dict = dict()

    for i in range(n):
        stored_dict[arr[i]] = i

    res = stored_dict.items()
    x = sorted(res, key=lambda y: y[1])
    print(len(x))
    for i in x:
        print(i[0], end=' ')