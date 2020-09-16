def fairRations(B):
    bread = 0
    total_bread = 0
    for i in range(len(B)):
        if i == len(B) - 1:
            total_bread += B[i]
            break
        if B[i] % 2 == 0:
            total_bread += B[i]
        else:
            B[i] = B[i] + 1
            B[i + 1] = B[i + 1] + 1
            bread += 2
            total_bread += B[i]

    if total_bread % 2 == 1:
        return 'NO'
    else:
        return bread



array = list(map(int, input().split()))
print(fairRations(array))