print('''Nessa aula, vamos aprender operações com String no Python. As principais operações que vamos aprender são o Fatiamento de String, Análise com len(), count(), find(), transformações com replace(), upper(), lower(), capitalize(), title(), strip(), junção com join().
''')

frase = 'Curso em Video Python'

print(frase[3])         # indice 3
print(frase[3:13])  # indice 3 ao 13
print(frase[:13])  # até o indice 13
print(frase[1:15])  # indice 1 ao 15
print(frase[1:15:2])  # indice 1 ao 15, com intervalo de 2
print(frase[1::2])  # indice 1 até o fim com intervalo de 2
print(frase[::2])  # do inicio ao fim com intervalo
print(frase.count('o'))  # conta "o" minusculo
print(frase.count('O'))  # conta "O" maiusculo
print(frase.upper().count('O'))  # transforma em maiusculo e depois conta "O"
print(len(frase))  # tamanho do vetor
print(len(frase.strip()))  # tamanho sem espaços no inicio e fim
print(frase.replace('Python', 'Android'))  # substitui palavras para impressão
# frase = frase.replace('Python', 'Android')  // substitui palavra na variável
print('Curso' in frase)  # Se palavra está contida
print(frase.find('Video'))  # encontre a posição da palavra exata
print(frase.lower().find('video')) # transforma o conteudo do vetor em minusculo para depois encontrar a palavra
print(frase.split()) # divide por espaçamento
dividido = frase.split() # armazena em lista
print(dividido[0]) #imprime um indice da lista