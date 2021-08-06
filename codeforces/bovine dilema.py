if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr_set = set()
        arr = list(map(int, input().split()))
        count = 0
        for i in range(n - 1):
            for j in range(i+1, n):
                area = arr[j] - arr[i]
                if area not in arr_set:
                    count += 1
                    arr_set.add(area)

        print(count)