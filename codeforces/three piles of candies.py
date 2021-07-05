if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        arr = list(map(int, input().split()))
        if sum(arr) % 2 == 1:
            print((sum(arr) - 1)//2)
        else:
            print(sum(arr)//2)