if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        if n == 2:
            print(2)
        else:
            if n % 2 == 0:
                print(0)
            else:
                print(1)
