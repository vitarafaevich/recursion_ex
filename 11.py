def index_maxlist(nums, index=0, max_index=0):
    if index == len(nums):
        return max_index
    if nums[index] > nums[max_index]:
        max_index = index
    return index_maxlist(nums, index + 1, max_index)


numbers = list(map(int, (input("enter the list items separated by a space ").split())))
print('the index of the largest is:', index_maxlist(numbers))
