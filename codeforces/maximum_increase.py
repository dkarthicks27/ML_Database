if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    increase = 1
    temp = 1
    for i in range(len(arr) - 1):
        if arr[i+1] > arr[i]:
            temp += 1
        else:
            increase = max(increase, temp)
            temp = 1


    if temp > increase:
        print(temp)
    else:
        print(increase)
