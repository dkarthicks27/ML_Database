from math import gcd

if __name__ == '__main__':
    a, b, n = list(map(int, input().split()))
    i = 0
    while True:
        if i % 2 == 0:
            stonesToRemove = gcd(a, n)
            if stonesToRemove <= n:
                n -= stonesToRemove
            else:
                print(1)
                break
        else:
            stonesToRemove = gcd(b, n)
            if stonesToRemove <= n:
                n -= stonesToRemove
            else:
                print(0)
                break

        i += 1
