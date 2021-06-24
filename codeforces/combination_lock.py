if __name__ == '__main__':
    n = int(input())
    x = input()
    y = input()
    moves = 0
    for i in range(n):
        a = int(x[i])
        b = int(y[i])
        moves += min(abs(a - b), 10 - abs(a - b))

    print(moves)