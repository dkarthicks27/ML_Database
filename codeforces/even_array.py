def solve(array):
    odd_mismatch = 0
    even_mismatch = 0
    for i in range(len(array)):
        if i % 2 == 0:
            if array[i] % 2 == 1:
                even_mismatch += 1
        else:
            if array[i] % 2 == 0:
                odd_mismatch += 1

    if odd_mismatch == even_mismatch:
        print(odd_mismatch)
    else:
        print(-1)



if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        r = list(map(int, input().split()))
        solve(r)