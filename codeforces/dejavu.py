if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        string = input()
        if set(string) == {'a'}:
            print('NO')
        else:
            print('YES')
            case1 = 'a' + string
            if case1 != case1[::-1]:
                print(case1)
            else:
                print(string+'a')