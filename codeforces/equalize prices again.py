if __name__ == '__main__':
    q = int(input())
    for _ in range(q):
        n = int(input())
        arr = list(map(int, input().split()))
        res = sum(arr)
        if len(set(arr)) == 1:
            print(arr[0])
        else:
            print(round(res / n))
