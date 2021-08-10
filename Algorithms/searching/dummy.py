def binary_search_insertion(item, arr):
    # handling border cases
    print(f'key: {item}, arr: {arr}')
    if arr[0] > item:
        new_arr = [item]
        new_arr.extend(arr)
        return new_arr
    elif arr[-1] < item:
        arr.append(item)
        return arr

    start = 0
    end = len(arr) - 1


    while start <= end:
        mid = (start + end) // 2
        if item > arr[mid]:
            start = mid + 1
        elif item < arr[mid]:
            end = mid - 1
        else:
            new_arr = arr[:mid] + [item] + arr[mid:]
            return new_arr
    new_arr = arr[:start] + [item] + arr[start:]
    return new_arr


res = binary_search_insertion(5, [2, 4, 4, 6, 7, 9])
print(res)
