precoNormal = float(input('Preço normal: '))

condicao = int(input(
    '\nQual a condição de pagamento:\n1 - Dinheiro/Cheque\n2 - Avista Cartão\n3 - 2x no Cartão\n4 - +3x no Cartão\nOpção: '))

if condicao == 1:
    print('\nPreço à vista em dinheiro/cheque R${}'.format(precoNormal*0.90))
elif condicao == 2:
    print('\nPreço à vista no cartão R${}'.format(precoNormal*0.95))
elif condicao == 3:
    print('\nPreço em até 2x no cartão R${}'.format(precoNormal))
elif condicao == 4:
    print('\nPreço em mais de 3x no cartão R${}'.format(precoNormal*1.20))
