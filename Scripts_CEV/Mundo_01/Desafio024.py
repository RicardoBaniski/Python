cidade = input('Digite o nome da cidade: ')

comeca = cidade.upper().find('SANTO')

if comeca == 0:
    print('Começa com SANTO')
else:
    print('Não começa com SANTO')
