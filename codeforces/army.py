if __name__ == '__main__':
    n = int(input())
    d_arr = list(map(int, input().split()))
    a, b = list(map(int, input().split()))

    tot = 0
    for i in range(a-1, len(d_arr)):
        if i == b - 1:
            break
        tot += d_arr[i]

    print(tot)