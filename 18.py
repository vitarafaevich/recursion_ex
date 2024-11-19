def simmetr(ln, strt, fnsh):
    if strt >= fnsh:
        return True
    elif ln[strt] == ln[fnsh]:
        return simmetr(ln, strt + 1, fnsh - 1)
    else:
        return False


line = input('enter the line of symbols: ')
start = int(input('enter the first index of the symmetric checking: '))
finish = int(input('enter the last index of the symmetric checking: '))
print('result', simmetr(line, start, finish))