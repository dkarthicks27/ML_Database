if __name__ == '__main__':
    # there are n candies and you must distribute them to two sisters alice and betty
    # alice will get a (a > 0) and betty will get b (b > 0)
    # a > b and a + b = n


    t = int(input())
    for _ in range(t):
        n = int(input())
        if n % 2 == 0:
            print(n // 2 - 1)
        else:
            print(n // 2)