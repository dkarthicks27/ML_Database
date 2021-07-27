if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        arr.sort(reverse=True)
        if arr[0] != arr[1]:
            print('NO')
        else:
            print('YES')
            print(arr[0], arr[2], arr[2])
