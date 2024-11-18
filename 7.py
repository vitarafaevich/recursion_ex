def nod(num_1, num_2):
    if num_1 == num_2:
        return num_1
    elif num_1 == 0 or num_2 == 0:
        if num_1 == 0:
            return num_2
        else:
            return num_1
    else:
        if num_1 < num_2:
            num_1, num_2 = num_2, num_1
        return nod(num_2, num_1 % num_2)


number_1 = int(input('enter the first number: '))
number_2 = int(input('enter the second number: '))
print('the largest common divisor of numbers', number_1, 'and', number_2, 'is:', nod(number_1, number_2))
