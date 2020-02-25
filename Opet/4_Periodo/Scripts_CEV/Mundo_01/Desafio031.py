distancia = int(input('Digite a distância: '))

if distancia <= 200:
    print('O preço da passagem é R${:.2f}'.format(0.5*distancia))
else:
    print('O preço da passagem é R${:.2f}'.format(0.45*distancia))
