

def smallerNumbersThanCurrent(nums):
    new_nums = sorted(nums)
    return [new_nums.index(i) for i in nums]




nums = [8, 1, 2, 2, 3]
x = smallerNumbersThanCurrent(nums)
print(x)
