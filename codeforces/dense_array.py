from math import ceil

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        # length of array is taken
        n = int(input())
        arr = list(map(int, input().split()))
        count = 0
        for i in range(n-1):
            if max(arr[i], arr[i+1]) <= 2 * min(arr[i], arr[i+1]):
                pass
            else:
                # print(f'i: {arr[i]}, i+1: {arr[i+1]}')
                p = max(arr[i], arr[i+1])
                q = min(arr[i], arr[i+1])
                while p > 2 * q:
                    count += 1
                    p = ceil(p / 2)
                    # print(f'p: {p}, count: {count}')
                # print('\n')

        print(count)