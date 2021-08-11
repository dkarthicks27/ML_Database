if __name__ == '__main__':
    n, c = list(map(int, input().split()))
    arr = list(map(int, input().split()))

    count = 1
    for i in range(1, n):
        if arr[i] - arr[i-1] > c:
            count = 1
        else:
            count += 1

    print(count)