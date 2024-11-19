def odd_list(nums):
    if not nums:
        return []
    if nums[0] % 2 == 0:
        return [nums[0]] + odd_list(nums[1:])
    else:
        return odd_list(nums[1:])


numbers = list(map(int, (input("enter the list items separated by a space ").split())))
print(odd_list(numbers))
