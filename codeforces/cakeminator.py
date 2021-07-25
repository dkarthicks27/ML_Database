import re


if __name__ == '__main__':
    r, c = list(map(int, input().split()))
    row_strawberry = set()
    col_strawberry = set()
    r_ = 0
    c_ = 0
    for i in range(r):
        demon = input()
        x = demon.count('S')
        if x:
            res = re.finditer(r'S', demon)
            for j in res:
                col = j.start()
                if i not in row_strawberry:
                    row_strawberry.add(i)
                    r_ += 1
                if col not in col_strawberry:
                    col_strawberry.add(col)
                    c_ += 1


    print(r * c - r_ * c_)
