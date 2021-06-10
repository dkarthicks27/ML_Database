def solve(arr, lower, upper):
    count = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if upper >= arr[i] + arr[j] >= lower:
                count += 1

    return count



if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, l, r = list(map(int, input().split()))
        li = list(map(int, input().split()))

        print(solve(li, l, r))