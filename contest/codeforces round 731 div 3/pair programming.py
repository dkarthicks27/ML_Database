from math import gcd

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        steps = 0
        if len(set(arr)) == 1:
            print(0)
        else:
            while True:
                if len(set(arr)) == 1:
                    break
                start = arr[0]
                for i in range(n):
                    if i == n - 1:
                        arr[i] = gcd(arr[i], start)
                    else:
                        arr[i] = gcd(arr[i], arr[i+1])
                steps += 1

            print(steps)