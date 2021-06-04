def solve(num):
    array = []
    while num:
        ans = num % pow(10, len(str(num)) - 1)
        array.append(num - ans)
        num = ans

    print(len(array))
    print(' '.join([str(i) for i in array]))



if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        solve(n)
