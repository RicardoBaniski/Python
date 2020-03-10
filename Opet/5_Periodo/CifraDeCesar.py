# ANDRESSA TONIETTO REIS - 1201800328
# RICARDO BANISKI - 1201800164

alfabeto = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz '


def criptografar(alfabeto, texto, chave):
    texto_criptografado = ''

    for caractere in texto:
        if caractere in alfabeto:
            index = alfabeto.find(caractere) + chave
            if index >= len(alfabeto):
                index -= len(alfabeto)
            texto_criptografado += alfabeto[index]
    return texto_criptografado


def descriptografar(alfabeto, texto_criptogradado, chave):
    texto = ''

    for caractere in texto_criptogradado:
        if caractere in alfabeto:
            index = alfabeto.find(caractere) - chave
            texto += alfabeto[index]
    return texto


def main():
    print('')
    print('Selecione uma opção:')
    print('1 - Codificar')
    print('2 - Decodificar')
    opc()


def opc():
    chave = int(input('\nInsira a chave: '))
    mensagem = input('Insira a mensagem: ')
    x = int(input('\nOpção: '))
    if(x == 1):
        c = criptografar(alfabeto, mensagem, chave)
        print('Texto Codificado: "', c, '"')
    elif (x == 2):
        dc = descriptografar(alfabeto, mensagem, chave)
        print('Texto Decodificado: "', dc, '"')
    else:
        print('\nOpção inválida')
    main()


if __name__ == "__main__":
    main()
