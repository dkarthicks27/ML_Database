if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        noOfZero = arr.count(0)
        if noOfZero == 0:
            if sum(arr) == 0:
                print(1)
            else:
                print(0)
        else:
            if sum(arr) + noOfZero == 0:
                print(noOfZero + 1)
            else:
                print(noOfZero)