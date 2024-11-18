def count(number):
    if number < 10:
        return 1
    else:
        return 1 + count(number//10)


num = int(input())
print('the number of digits is:', count(num))
