def search(nums, x):
    if len(nums) == 0:
        return 0
    if (nums[len(nums) - 1]) != x:
        del nums[len(nums) - 1]
        return search(nums, x)
    else:
        return 1


numbers = list(map(int, (input("enter the list items separated by a space ").split())))
x = int(input('enter the number u want to find in the list '))
print(search(numbers, x))
