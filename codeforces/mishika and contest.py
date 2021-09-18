if __name__ == '__main__':
    n, k = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    curr_end = True
    count = 0
    while curr_end:
        if len(arr) == 0:
            curr_end = False
        elif arr[0] <= k:
            arr.pop(0)
            count += 1
        elif arr[len(arr) - 1] <= k:
            arr.pop()
            count += 1
        else:
            curr_end = False


    print(count)