def solve(arr1, arr2, n):
    k = set()
    count = 0
    for i in range(n):
        if (arr1[i], arr2[i]) in k:
            count += 1
        else:
            k.add((arr2[i], arr1[i]))

    print(2*pow(2, count) % (10 ** 9 + 7))



if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        li1 = list(map(int, input().split()))
        li2 = list(map(int, input().split()))
        solve(li1, li2, n)