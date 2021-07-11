if __name__ == '__main__':
    n = int(input())
    if n % 2 == 1:
        print(-1)
    else:
        arr = [i for i in range(1, n+1)]
        for i in range(0, n-1, 2):
            temp = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = temp

        print(' '.join(map(str, arr)))