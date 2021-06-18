if __name__ == '__main__':
    n = int(input())
    if n == 2:
        print(1)
    else:
        count = 0
        for l in range(1, n//2 + 1):
            if (n - l) % l == 0:
                count += 1

        print(count)
