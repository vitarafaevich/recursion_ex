def progress(first, dif, number):
    if number == 1 or dif == 0:
        return first
    elif number <= 0:
        return ValueError
    else:
        return first + progress(first + dif, dif, number - 1)


frst = int(input('enter the first number of the progression: '))
df = int(input('enter the difference between the progression numbers: '))
num = int(input('enter the ordinal number of the numbers in the progression whose total number you want to know: '))
print('the total of', num, 'numbers in the progression is:', progress(frst, df, num))
