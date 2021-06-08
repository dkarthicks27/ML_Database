def solve(array):
    array.sort()
    min_val = array[1] - array[0]
    for i in range(len(array) - 1):
        if array[i+1] - array[i] < min_val:
            min_val = array[i+1] - array[i]

    return min_val


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = input()
        arr = list(map(int, input().split()))
        print(solve(arr))