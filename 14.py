def numbers(num):
    if num < 10:
        print(num)
    else:
        print(num%10)
        numbers(num//10)


number = int(input('enter the list items separated by a space '))
print(numbers(number))
