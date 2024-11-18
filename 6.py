def degree_5(num):
    if num == 1:
        return 0
    elif num%5 != 0:
        return -1
    else:
        check = degree_5(num/5)
        if check != -1:
            return 1 + degree_5(num/5)
        else:
            return -1


number = int(input('enter the number: '))
print(number, 'is 5 to the degree of', degree_5(number))
