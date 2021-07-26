if __name__ == '__main__':
    n = int(input())
    tot = sum([int(i) for i in str(n)])
    while not tot % 4 == 0:
        n += 1
        tot = sum([int(i) for i in str(n)])

    print(n)