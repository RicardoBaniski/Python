preco = int(input('Preço: '))
d = 5

desconto = preco * (d/100)

total = preco - desconto

print('Desconto de {}'.format(desconto))
print('O total é {}'.format(total))
