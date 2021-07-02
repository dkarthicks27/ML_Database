def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


if __name__ == '__main__':
    a, b = list(map(int, input().split()))
    print(factorial(min(a, b)))