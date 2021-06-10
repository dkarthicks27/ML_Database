def solve(arr, len_arr):
    min_pos = arr.index(min(arr))
    max_pos = arr.index(max(arr))
    if min_pos < round(len_arr / 2):
        if max_pos > round(len_arr / 2):
            return min_pos + len_arr - 1 - max_pos + 2
        else:
            return max(min_pos, max_pos) + 1
    else:
        if max_pos < round(len_arr / 2):
            return len_arr - 1 - min_pos + max_pos + 2
        else:
            return max(len_arr - 1 - min_pos, len_arr - 1 - max_pos) + 1




if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))

        print(solve(a, n))
