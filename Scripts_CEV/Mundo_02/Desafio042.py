print('Digite os lados de um Triangulo')

a = int(input('Lado A: '))
b = int(input('Lado B: '))
c = int(input('Lado C: '))

if a == b and b == c and c == a:
    print('Triangulo Equilátero')
elif a != b and b != c and c != a:
    print('Triangulo Escaleno')
else:
    print('Triangulo Isósceles')