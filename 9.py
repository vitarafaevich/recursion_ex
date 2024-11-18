def combin(n, k):
    if n == k or k == 0:
        return 1
    else:
        return combin(n - 1, k) + combin(n - 1, k - 1)


nn = int(input('enter n: '))
kk = int(input('enter k: '))
print('combinatorial combination of n by k:', combin(nn, kk))