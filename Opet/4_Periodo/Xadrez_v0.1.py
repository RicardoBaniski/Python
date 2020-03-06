# Ricardo Baniski 1201800164

import random

infantil = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N'
]
juvenil = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N'
]
adulto = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N'
]


def cadastrar():
    nome = input('\nNome: ')
    idade = int(input('Idade: '))
    if (idade < 8):
        print('Idade insuficiente')
    elif (idade >= 8) and (idade < 13):
        infantil.append(nome)
        print('Falta(m) {} jogador(es) na Categoria Infantil'.format(
            16 - len(infantil)))
    elif (idade >= 13) and (idade < 18):
        juvenil.append(nome)
        print('Falta(m) {} jogador(es) na Categoria Juvenil'.format(16 - len(juvenil)))
    else:
        adulto.append(nome)
        print('Falta(m) {} jogador(es) na Categoria Adulto'.format(16 - len(adulto)))
    menuPrincipal()


def chave():
    print('''
  1. Infantil
  2. Juvenil
  3. Adulto
  ''')
    opc = int(input('Opcão: '))
    if (opc == 1):
        random.shuffle(infantil)
        print('TORNEIO INFANTIL:')
        for x in range(0, 8):
            print('Partida: ', x, (infantil[x]), 'x', (infantil[8+x]))
    elif (opc == 2):
        random.shuffle(juvenil)
        print('Partida JUVENIL:')
        for x in range(0, 8):
            print('Chave: ', x, (juvenil[x]), 'x', (juvenil[8+x]))
    elif (opc == 3):
        random.shuffle(adulto)
        print('\nTORNEIO ADULTO')
        for x in range(0, 8):
            print('Partida: ', x, (adulto[x]), 'x', (adulto[8+x]))
    menuPrincipal()


def menuPrincipal():
    print(''' 
1. Registrar um participante. 
2. Verificar Chave do torneio. 
''')
    opc = int(input('Opção: '))
    if(opc == 1):
        cadastrar()
    if(opc == 2):
        chave()


menuPrincipal()
