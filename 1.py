def pownum(number, deg):
    if deg == 0:
        return 1
    elif deg == 1:
        return number
    else:
        return number * pownum(number, deg - 1)


num = int(input('enter the number: '))
dg = int(input('enter the degree: '))
print('result:', pownum(num, dg))


