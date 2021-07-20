if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    biceps = 0
    chest = 0
    back = 0
    k = 0
    for i in range(len(arr)):
        if k == 0:
            chest += arr[i]
            k += 1
        elif k == 1:
            biceps += arr[i]
            k += 1
        elif k == 2:
            back += arr[i]
            k = 0

    val = max(biceps, chest, back)
    if val == biceps:
        print('biceps')
    elif val == chest:
        print('chest')
    else:
        print('back')