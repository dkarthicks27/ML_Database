def get_count(arr):
    count = arr[0] + arr[-1]
    for i in range(1, len(arr)):
        count += abs(arr[i] - arr[i - 1])

    return count


def solve(arr):
    count = get_count(arr)
    # print(f'count: {count}')
    li_set = set(arr)
    # print(li_set)
    while li_set:
        min_arr = min(li_set)
        tot = sum([abs(i - min_arr) for i in arr if i > min_arr])
        new_arr = []
        for i in arr:
            if i > min_arr:
                new_arr.append(min_arr)
            else:
                new_arr.append(i)

        # print(f'new_count: {get_count(new_arr)}, wh: {tot + get_count(new_arr)}')
        if tot + get_count(new_arr) < count:
            count = tot + get_count(new_arr)
        # print(f'count: {count}\n')
        li_set.remove(min_arr)

    print(count)



if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        n = int(input())
        li = list(map(int, input().split()))
        solve(li)