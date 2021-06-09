if __name__ == '__main__':
    n = int(input())
    p = list(map(int, input().split()))
    p = set(p[1:])
    q = list(map(int, input().split()))
    q = set(q[1:])

    if list(p.union(q)) == list(range(1, n+1)):
        print("I become the guy.")
    else:
        print("Oh, my keyboard!")