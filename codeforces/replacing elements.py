if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, d = list(map(int, input().split()))
        arr = list(map(int, input().split()))
        arr.sort()
        if sum([1 for i in arr if i <= d]) == n:
            print('yes')
        elif arr[0] + arr[1] <= d:
            print('yes')
        else:
            print('no')