def calc(array):
    ref = set(array)
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if abs(array[i] - array[j]) not in ref:
                ref.add(abs(array[i] - array[j]))

    return list(ref)


def is_nice(array):
    while len(array) <= 300:
        x = calc(array)
        if array == x:
            return ['YES', len(array), array]
        array = x

    return ['NO']




if __name__ == '__main__':
    t = int(input())
    li = []
    for _ in range(t):
        n = input()
        ar = list(map(int, input().split()))
        li.append(ar)

    for arr in li:
        ans = is_nice(array=arr)
        if ans[0] == 'YES':
            print('YES')
            print(ans[1])
            print(' '.join(str(p) for p in ans[2]))
        else:
            print('NO')
