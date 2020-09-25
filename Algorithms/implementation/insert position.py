def binary_search(array, target):
    start = 0
    end = len(array) - 1

    while start <= end:
        mid = round((start + end) / 2)
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return start


arr = [1, 3, 5, 6]

print(binary_search(arr, 5.5))
