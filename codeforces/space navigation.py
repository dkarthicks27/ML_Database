import re

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        x, y = list(map(int, input().split()))
        control = input()
        check_x = False
        check_y = False
        if x > 0:
            r = len(''.join(re.findall(r'R+', control)))
            if r >= x:
                check_x = True
        elif x < 0:
            l = len(''.join(re.findall(r'L+', control)))
            if -1 * l <= x:
                check_x = True
        else:
            check_x = True

        if y > 0:
            u = len(''.join(re.findall(r'U+', control)))
            if u >= y:
                check_y = True
        elif y < 0:
            d = len(''.join(re.findall(r'D+', control)))
            if -1 * d <= y:
                check_y = True
        else:
            check_y = True

        if check_x and check_y:
            print('YES')
        else:
            print('NO')