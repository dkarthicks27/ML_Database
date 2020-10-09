def maximumStones(arr):
    sumOdd = 0
    sumEven = 0

    for i in range(len(arr)):
        if i % 2 == 0:
            sumOdd += arr[i]
        else:
            sumEven += arr[i]

    return min(sumEven, sumOdd) * 2


print(maximumStones([2, 1, 2]))
