def sort(nums):
    for i in range(len(nums)):
        minPos = i

        for j in range(i, len(nums)):
            if nums[j] < nums[minPos]:
                minPos = j

        nums[minPos], nums[i] = nums[i], nums[minPos]



nums = [5, 2, 3, 8, 19, -2]
sort(nums)

print(nums)
