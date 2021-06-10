def solve(low, upp):
    XOR = low ^ upp
    print(XOR)
    result = bin(XOR).count("1")
    print(result, '\n')
    pass


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        l, r = list(map(int, input().split()))
        solve(l, r)