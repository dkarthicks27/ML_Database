if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    sum1 = 0
    sum2 = 0
    i = 0
    while arr:
        if i % 2 == 0:
            ele1 = arr[0]
            ele2 = arr[len(arr) - 1]
            if ele2 > ele1 or ele1 == ele2:
                sum1 += arr.pop()

            else:
                sum1 += arr[0]
                arr.remove(arr[0])

        else:
            ele1 = arr[0]
            ele2 = arr[len(arr) - 1]
            if ele2 > ele1 or ele1 == ele2:
                sum2 += arr.pop()

            else:
                sum2 += arr[0]
                arr.remove(arr[0])

        i += 1

    print(sum1, sum2)