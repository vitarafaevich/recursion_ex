def maxlist(nums):
    if len(nums) == 1:
        return nums
    if (nums[len(nums) - 1]) > (nums[len(nums) - 2]):
        del nums[len(nums) - 2]
        return maxlist(nums)
    else:
        del nums[len(nums) - 1]
        return maxlist(nums)


numbers = list(map(int, (input("enter the list items separated by a space ").split())))
print('the largest is:', maxlist(numbers))

