def check_if_cake(x, y, d):
    diff_x = x - 1
    diff_y = y - 1
    res = diff_x + diff_y * x
    if res == d:
        print('YES')
    else:
        print('NO')




if __name__ == '__main__':
    for _ in range(int(input())):
        x, y, z = list(map(int, input().split()))
        check_if_cake(x, y, z)
