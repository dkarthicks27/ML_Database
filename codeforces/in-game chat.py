if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        string = input()
        count = 0
        i = n-1
        while string[i] == ')' and i >= 0:
            count += 1
            i -= 1

        if 2 * count > n:
            print('yes')
        else:
            print('no')
