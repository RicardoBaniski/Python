import random

nome = []

i = 1
while (i <= 4):
    nome.append(input('Digite o nome: '))
    i += 1

random.shuffle(nome)
print('O escolhido foi {}'.format(nome[0]))
