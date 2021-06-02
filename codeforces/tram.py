if __name__ == '__main__':
    n = int(input())
    curr = 0
    capacity = -1

    for _ in range(n):
        leave, enter = list(map(int, input().split()))
        curr = curr - leave
        curr = curr + enter
        if curr > capacity:
            capacity = curr

    print(capacity)