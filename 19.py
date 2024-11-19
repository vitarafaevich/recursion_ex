def count(a, b):
    if a == b:
        return 1
    elif a > b:
        return 1 + count(a-b, b)
    else:
        return 1 + count(a, b-a)


first_side = int(input('enter first side'))
second_side = int(input('enter second side'))
print(count(first_side, second_side))
