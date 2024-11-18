def fib(num):
    if num < 0:
        return ValueError
    elif num == 1:
        return 0
    elif num == 2 or num == 3:
        return 1
    else:
        return fib(num - 2) + fib(num - 1)


number = int(input('enter the number of the member of Fibonacci sequence you want to find: '))
print('result:', fib(number))
