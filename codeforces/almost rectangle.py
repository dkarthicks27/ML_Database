import re

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        points = []
        arr = []
        for i in range(n):
            x = input()
            arr.append(x)
            if len(points) < 2:
                res = list(re.finditer(r'\*', x))
                if len(res) == 2:
                    # same row
                    points.extend([(i, k.start()) for k in res])
                elif res:
                    points.append((i, res[0].start()))

        x, y = points
        if x[0] == y[0]:
            # same row
            # we can print two * in any other row
            ast = 0
            for i in range(len(arr)):
                if i != x[0] and ast == 0:
                    string = list(arr[i])
                    string[x[1]] = '*'
                    string[y[1]] = '*'
                    arr[i] = ''.join(string)
                    ast += 1

        elif x[1] == y[1]:
            # we need to choose any other column other than x[1]
            col_no = list(range(n))
            col_no.remove(x[1])
            col_no = col_no[0]
            ast = 0
            for i in range(len(arr)):
                if x[0] == i and ast < 2:
                    string = list(arr[i])
                    string[col_no] = '*'
                    arr[i] = ''.join(string)
                    ast += 1

                if y[0] == i and ast < 2:
                    string = list(arr[i])
                    string[col_no] = '*'
                    arr[i] = ''.join(string)
                    ast += 1

        else:
            ast = 0
            for i in range(n):
                if x[0] == i and ast < 2:
                    string = list(arr[i])
                    string[y[1]] = '*'
                    arr[i] = ''.join(string)
                    ast += 1
                elif y[0] == i and ast < 2:
                    string = list(arr[i])
                    string[x[1]] = '*'
                    arr[i] = ''.join(string)
                    ast += 1

        for i in arr:
            print(i)


    # so there might be 3 cases same row, same column, diff places

    # so if same rows then print in parallel position in any other row
    # same column then replace any other parallel . with *
