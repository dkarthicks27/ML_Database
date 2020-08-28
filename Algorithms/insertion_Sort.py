def sort(array):
    for i in range(1, len(array)):
        curElement = array[i]
        pos = i


        while pos > 0 and array[pos - 1] > curElement:
            array[pos] = array[pos - 1]
            pos -= 1

        array[pos] = curElement

    return array


nums = list(map(int, input().split()))
nums_Sorted = sort(nums)

print(nums_Sorted)