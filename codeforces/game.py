if __name__ == '__main__':
    n1, n2, k1, k2 = list(map(int, input().split()))
    i = 1
    while True:
        if i % 2 == 1:
            n1 -= 1
        else:
            n2 -= 1
        i += 1

        if n1 == 0:
            print('Second')
            break
        elif n2 == 0:
            print('First')
            break
