def ten_to_bin(num):
    if num == 0:
        return []
    if num % 2 == 0:
        return [0] + ten_to_bin(num/2)
    else:
        return [1] + ten_to_bin(num//2)


number = int(input('enter a number to transfer it to the x2 system '))
res = ten_to_bin(number)
result = ''.join(map(str, res[::-1]))
print('result:', result)