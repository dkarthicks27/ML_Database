if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        x, req_rem, z = list(map(int, input().split()))
        rem = z % x
        if rem == req_rem:
            print(z)
        elif rem > req_rem:
            print(z - (rem - req_rem))
        else:
            k = z - x + (req_rem - rem)
            print(k)

