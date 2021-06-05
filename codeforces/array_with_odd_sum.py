if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        n = input()
        li = list(map(int, input().split()))
        odd_count = 0
        even_count = 0

        for i in li:
            if i % 2 == 0:
                even_count += 1
            else:
                odd_count += 1

        if odd_count % 2 == 1:
            print('YES')
        else:
            if even_count > 0 and odd_count > 0:
                print('YES')
            else:
                print('NO')