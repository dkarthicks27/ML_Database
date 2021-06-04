if __name__ == '__main__':
    n = int(input())
    string = input().lower()

    if len(set([i for i in string])) == 26:
        print('YES')
    else:
        print('NO')

j