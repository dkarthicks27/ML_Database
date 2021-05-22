if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    snake_cell = '#'
    empty_cell = '.'

    for i in range(1, n+1):
        if i % 2 == 1:
            print(snake_cell * m)
        else:
            k = (i - 2)/4 + 1
            if k.is_integer():
                print(empty_cell * (m - 1), snake_cell, sep='')
            else:
                print(snake_cell, empty_cell * (m - 1), sep='')