def two_to_sixteen(x, n):
    digits = "0123456789ABCDEF"
    if x < n:
        return digits[x]
    else:
        return two_to_sixteen(x // n, n) + digits[x % n]


x = int(input('enter a number to transfer it to the x2 system '))
n = int(input('in what system are we going '))

print(two_to_sixteen(x, n))


'''
def two_nine_to_bin(x, n):
    if 1 < n < 11:
        if x == 0:
            return []
        if x % n == 0:
            return [0] + two_nine_to_bin(x//n, n)
        else:
            return [x % n] + two_nine_to_bin(x//n, n)
    elif 11 <= n <= 16:
        eleven_to_sixteen(x, n)


def eleven_to_sixteen(x, n):
    digits = "0123456789ABCDEF"
    if x < n:
        return digits[x]
    else:
        return eleven_to_sixteen(x // n, n) + digits[x % n]


x = int(input('enter a number to transfer it to the x2 system '))
n = int(input('in what system are we going '))

res = two_nine_to_bin(x, n)
result = ''.join(map(str, res[::-1]))
print(result)
'''