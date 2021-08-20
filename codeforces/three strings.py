def check_three_strings(x, y, z):
    for i in range(len(x)):
        if x[i] == y[i]:
            if x[i] != z[i]:
                return 'NO'
        elif x[i] == z[i] or y[i] == z[i]:
            continue
        else:
            return 'NO'
    return 'YES'



if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        a = input()
        b = input()
        c = input()

        print(check_three_strings(a, b, c))
