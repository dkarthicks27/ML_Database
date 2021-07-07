if __name__ == '__main__':
    n, x = list(map(int, input().split()))
    d_kids = 0
    for i in range(n):
        sign, val = input().split()
        if sign == '+':
            x += int(val)
        else:
            if x >= int(val):
                x -= int(val)
            else:
                d_kids += 1

    print(x, d_kids)