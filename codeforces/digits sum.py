if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        if n < 9:
            print(0)
        else:
            if int(str(n)[-1]) == 9:
                print(n//10 + 1)
            else:
                print(n // 10)