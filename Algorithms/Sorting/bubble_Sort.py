nums = list(map(int, input().split()))


def sort(n):
    for i in range(len(n) - 1, 0, -1):
        array_sorted = True
        for j in range(i):
            if n[j] > n[j + 1]:
                n[j], n[j + 1] = n[j + 1], n[j]

                array_sorted = False

        if array_sorted:
            break


sort(nums)

print(nums)
