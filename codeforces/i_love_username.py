if __name__ == '__main__':
    n = int(input())
    li = list(map(int, input().split()))

    high = li[0]
    low = li[0]

    amazing = 0
    for i in li:
        if i > high:
            high = i
            amazing += 1
        elif i < low:
            amazing += 1
            low = i


    print(amazing)
