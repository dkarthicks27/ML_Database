
if __name__ == '__main__':
    rooms = int(input())
    count = 0
    for _ in range(rooms):
        p, q = list(map(int, input().split()))
        if q - p >= 2:
            count += 1

    print(count)