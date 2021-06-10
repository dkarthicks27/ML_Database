def solve(arr):
    mean = sum(arr) / len(arr)

    if mean.is_integer():
        return sum([1 for i in arr if i > mean])
    else:
        return -1



if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        li = list(map(int, input().split()))
        print(solve(li))