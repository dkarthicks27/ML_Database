def solve(a, b, k):
    a.sort()
    b.sort()
    i = -1
    j = 0
    for moves in range(k):
        if a[j] < b[i]:
            temp = a[j]
            a[j] = b[i]
            b[i] = temp
            # b.pop()
            # b.append(temp)
            i -= 1
            j += 1


    print(sum(a))




if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        n, k_ = list(map(int, input().split()))
        a_ = list(map(int, input().split()))
        b_ = list(map(int, input().split()))
        solve(a_, b_, k_)
