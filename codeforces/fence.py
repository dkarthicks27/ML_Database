if __name__ == '__main__':
    n, h = list(map(int, input().split()))

    array = list(map(int, input().split()))

    count = 0
    for i in array:
        if i > h:
            count += 2
        else:
            count += 1

    print(count)