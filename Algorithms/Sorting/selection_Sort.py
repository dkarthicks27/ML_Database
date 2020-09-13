def sort(num):
    for i in range(len(num)):
        minPos = i

        for j in range(i, len(num)):
            if num[j] < num[minPos]:
                minPos = j

        num[minPos], num[i] = num[i], num[minPos]



nums = [5, 2, 3, 8, 19, -2]
sort(nums)

print(nums)

