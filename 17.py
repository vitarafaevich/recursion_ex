def function1(n):
    if is_it_prime(n):
        return 1
    else:
        return 0


def is_it_prime(n, i=2):
    if n <= 2:
        return True if n == 2 else False
    if n % i == 0:
        return False
    if i * i > n:
        return True
    return is_it_prime(n, i + 1)


n = int(input('what number u want to check? '))
print('result', function1(n))
