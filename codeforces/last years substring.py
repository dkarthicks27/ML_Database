import re


if __name__ == '__main__':
    # possible strings are 2020, 2.*020, 20.*20, 202.*0
    t = int(input())
    for _ in range(t):
        n = int(input())
        string = input()
        pattern = [r'^2020', r'2020$', r'^2.*020$', r'^20.*20$', r'^202.*0$']
        q = 0
        for i in pattern:
            if re.search(i, string):
                print('YES')
                q = 1
                break

        if q == 0:
            print('NO')


