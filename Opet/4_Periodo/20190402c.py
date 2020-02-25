print('Exemplo 09')


def sub(x, y):
    r = x-y
    return r


print(sub(10, 5))


print('\nExemplo 10')


def soma(x, y):
    return x + y


print(soma(10, 5))


print('\nExemplo 11')


def minMax(v):
    minimo = v[0]
    maximo = v[0]
    for elemento in v:
        if elemento > maximo:
            maximo = elemento
        if elemento < minimo:
            minimo = elemento
    return minimo, maximo


print(minMax([5, 7, 2, 9, 1]))
x, y = minMax([7, 2, 5, 4])
print(x)
print(y)


print('\nExemplo 12')


def fat(n):
    if n in (0, 1):
        return 1
    return fat(n-1)*n


print(fat(5))


print('\nExemplo 13')


def soma(x, y):
    return x + y


def sl(x, y): return x + y


print(soma(5, 10))
print(sl(5, 10))


print('\nExemplo 14')


def p(x): return x % 2


if p(2):
    print('oi')
