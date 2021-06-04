def solve(string):
    if len(string) > 2:
        base = string[0:2]
        for i in range(2, len(string)):
            if i % 2 != 0:
                base += string[i]

        print(base)

    else:
        print(string)


if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        inp = input()
        solve(inp)