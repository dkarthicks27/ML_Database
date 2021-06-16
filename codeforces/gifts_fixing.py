def solve(a, b):
    moves = 0
    min_a = min(a)
    min_b = min(b)
    for i in range(len(a)):
        if a[i] > min_a and b[i] > min_b:
            mva = -min_a + a[i]
            mvb = -min_b + b[i]
            x = min(mva, mvb)
            moves += x + (mva - x) + (mvb - x)
        elif a[i] > min_a:
            moves += a[i] - min_a
        elif b[i] > min_b:
            moves += b[i] - min_b

    return moves


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        print(solve(a, b))
