def solve(arr, k):
    largest = max(arr)
    new_arr = [largest - i for i in arr]
    if k % 2 == 1:
        return new_arr
    else:
        largest = max(new_arr)
        return [largest - i for i in new_arr]


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, k = list(map(int, input().split()))
        arr = list(map(int, input().split()))
        ret_arr = solve(arr, k)
        print(' '.join(map(str, ret_arr)))