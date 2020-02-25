import random

nome = []

i = 1
while (i <= 4):
    nome.append(input('Digite o nome: '))
    i += 1

random.shuffle(nome)
print('\n1º {} \n2º {} \n3º {} \n4º {}\n'.format(
    nome[0], nome[1], nome[2], nome[3]))
