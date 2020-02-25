nome = str(input('Qual é seu nome? '))
if nome == 'Ricardo':
    print('Seu nome é igual ao meu!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem comum!')
else:
    print('Parabéns pelo nome!')
print('Tenha um bom dia, {}'.format(nome))
