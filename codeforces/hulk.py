if __name__ == '__main__':
    n = int(input())
    if n == 1:
        print('I hate it')
    else:
        odd = 'I hate'
        even = 'I love'

        for i in range(1, n+1):
            if i % 2 == 1:
                if i == n:
                    print(odd, 'it', end='')
                else:
                    print(odd, 'that', end=' ')
            else:
                if i == n:
                    print(even, 'it', end='')
                else:
                    print(even, 'that', end=' ')


