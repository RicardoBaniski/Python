frase = input('Digite uma frase: ')

print('Número de ocorrências: {}'.format(frase.upper().count('A')))
print('Primeira ocorrência: {}'.format(frase.upper().index('A')))
print('Última ocorrência: {}'.format((len(frase)-1)-frase[::-1].upper().index('A')))
