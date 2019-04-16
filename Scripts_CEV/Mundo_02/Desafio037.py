numero = int(input('Digite um numero: '))

opc = int(input('\n1 - binário\n2 - octal\n3 - hexadecimal\nOpção: '))

if opc == 1:
    print('Número convertido para binário: {}'.format(bin(numero)))
elif opc == 2:
    print('Número convertido para octal: {}'.format(oct(numero)))
elif opc == 3:
    print('Número convertido para Hexadecimal: {}'.format(hex(numero)))
else:
    print('Nenhuma das opções acima')