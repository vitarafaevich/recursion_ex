def progress(first, dif, number):
    if number == 1 or dif == 0:
        return first
    elif number <= 0:
        return ValueError
    else:
        return progress(first + dif, dif, number - 1)


frst = int(input('enter the first number of the progression: '))
df = int(input('enter the difference between the progression numbers: '))
num = int(input('enter the sequence number of the numbers in the progression u want to know: '))
print('the', num, 'number of the progression is:', progress(frst, df, num))
