if __name__ == '__main__':
    arr = list(map(int, input().split()))
    li = [max(arr) - i for i in arr]
    for i in li:
        if i != 0:
            print(i, end=' ')
