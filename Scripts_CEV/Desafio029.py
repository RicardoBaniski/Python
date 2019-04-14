velocidade = int(input('Qual a velocidade do carro: '))

if velocidade > 80:
    print('Você foi multado em R${:.2f} por excesso de velocidade'.format((velocidade-80)*7))
else:
    print('Você esta dentro do limite de velocidade')
