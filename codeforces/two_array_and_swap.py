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



def solve2(a, b, k):
    a.sort()
    b.sort(reverse=True)
    tot = 0
    for i in range(len(a)):
        if i < k:
            tot += max(a[i], b[i])
        else:
            tot += a[i]

    print(tot)


if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        n, k_ = list(map(int, input().split()))
        a_ = list(map(int, input().split()))
        b_ = list(map(int, input().split()))
        solve2(a_, b_, k_)
