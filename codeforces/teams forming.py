if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    # here every two pair are considered

    count = 0
    for i in range(0, n, 2):
        count += arr[i+1] - arr[i]

    print(count)
