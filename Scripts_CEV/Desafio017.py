import math

ca = int(input('Cateto Adjacente: '))
co = int(input('Cateto Oposto: '))

h = math.hypot(ca,co)

print('Hipotenusa = {}'.format(h))