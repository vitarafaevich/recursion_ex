def mod_number(nat_1, nat_2):
    if nat_1 < nat_2:
        return nat_1
    else:
        return mod_number(nat_1 - nat_2, nat_2)


num_1 = int(input('enter the first natural number '))
num_2 = int(input('enter the second natural number '))

print('the remainder of the division is', mod_number(num_1, num_2))
