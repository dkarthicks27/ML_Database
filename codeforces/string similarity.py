if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        string = input()
        if n == 1:
            print(string)
        else:
            print(''.join([string[i] for i in range(0, 2*n - 1, 2)]))