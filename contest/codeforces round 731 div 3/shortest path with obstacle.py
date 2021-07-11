if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        i = input()
        xa, xb = list(map(int, input().split()))
        ya, yb = list(map(int, input().split()))
        za, zb = list(map(int, input().split()))


        if xa == ya:
            if xb == yb:
                print(0)
            elif zb in range(min(xb, yb)+1, max(xb, yb)+1) and za == xa:
                print(abs(xa - ya) + abs(xb - yb) + 2)
            else:
                print(abs(xa - ya) + abs(xb - yb))

        elif xb == yb:
            if xa == ya:
                print(0)
            elif za in range(min(xa, ya)+1, max(xa, ya)+1) and zb == xb:
                print(abs(xa - ya) + abs(xb - yb) + 2)
            else:
                print(abs(xa - ya) + abs(xb - yb))

        else:
            print(abs(xa - ya) + abs(xb - yb))

