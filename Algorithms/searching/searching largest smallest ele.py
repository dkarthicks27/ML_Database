def binarySearch(arr, q):
    print(arr)
    arr.sort()
    # print(arr)
    start = 0
    end = len(arr) - 1
    ans = -1
    while start <= end:
        # print((start, end))
        mid = (start + end)//2
        # print(mid)
        if arr[mid] < q:
            ans = mid
            start = mid + 1
        elif arr[mid] > q:
            end = mid - 1
    return ans



arr = [13, 20, 15, 8, 2, 12]


for i, val in enumerate(arr):
    print(f'i: {i}, val: {val}')
    binary = binarySearch(arr[i+1:], val)
    print(arr)
    if binary != -1:
        print('index is:', binary + i+1, 'val is:', arr[binary+i + 1])
    else:
        print('no such index found')
    print('\n')
