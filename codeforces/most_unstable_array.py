# n, m -- > make array of len =n ,such that sum(array) = m

# also array a = [a1, a2, a3 ..., an] , then
# |a1 - a2| + |a2 - a3| +....+ |an-1 + an| is max


# it is given a1 + a2 + a3 + .... + an = m

# [1 2 3 4 5 6 7 8 9 10] sum is 10
# 10 =


# so the most obvious thing is that, the best way to construct an array is

# [0, m, 0, 0, ... , ]
# which means that if n == 2: then [0, m ] gives us sum = m
# otherwise we have [0, m, 0 ] sub part where sum is 2m because (m - 0) + (m - 0) hence we need to

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = list(map(int, input().split()))
        if n == 1:
            print(0)
        else:
            print(min(2, n - 1) * m)



