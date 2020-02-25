import random

jokenpo = [1, 2, 3]
maquina = int(random.choice(jokenpo))
usuario = int(input('\nEscolha:\n1 - Pedra\n2 - Papel\n3 - Tesoura\nOpção: '))

if usuario == maquina:
    print('\nEMPATE\n')
elif usuario == 1 and maquina == 2:
    print('\nPedra X Papel\nVocê perdeu!\n')
elif usuario == 2 and maquina == 3:
    print('\nPapel X Tesoura\nVocê perdeu!\n')
elif usuario == 3 and maquina == 1:
    print('\nTesoura X Pedra\nVocê perdeu!\n')
elif usuario == 1 and maquina == 3:
    print('\nPedra X Tesoura\nVocê ganhou!\n')
elif usuario == 2 and maquina == 1:
    print('\nPapel X Pedra\nVocê ganhou!\n')
elif usuario == 3 and maquina == 2:
    print('\nTesoura X Papel\nVocê ganhou!\n')
