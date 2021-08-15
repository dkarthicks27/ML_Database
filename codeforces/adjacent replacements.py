if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    for i in range(n):
        if arr[i] % 2 == 0:
            arr[i] -= 1

    print(' '.join(map(str, arr)))