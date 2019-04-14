print('Digite os lados do Triangulo')
a = int(input('Lado A: '))
b = int(input('Lado B: '))
c = int(input('Lado C: '))

if((b - c) < a) and (a < (b + c)):
    if((a - c) < b) and (b < (a + c)):
        if((a - b) < c) and (c < (a + b)):
            print('\nPARABÉNS, é um Triangulo')
else:
    print('\nNão é possível formar um Triangulo com essas medidas')
