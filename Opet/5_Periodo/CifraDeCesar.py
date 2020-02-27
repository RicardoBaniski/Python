class Cifra(object):

    def __init__(self):
        self._alfabeto = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz '

    def criptografar(self, texto, chave):
        texto_criptografado = ''

        for caractere in texto:
            if caractere in self._alfabeto:
                index = self._alfabeto.find(caractere) + chave
                if index >= len(self._alfabeto):
                    index -= len(self._alfabeto)
                texto_criptografado += self._alfabeto[index]
        return texto_criptografado

    def descriptografar(self, texto_criptogradado, chave):
        texto = ''

        for caractere in texto_criptogradado:
            if caractere in self._alfabeto:
                index = self._alfabeto.find(caractere) - chave
                texto += self._alfabeto[index]
        return texto


if __name__ == '__main__':
    cifra = Cifra()
    chave = int(input('\nInsira a chave: '))
    mensagem = input('Insera a mensagem: ')
    modo = input(
        '\nPara:\n- CODIFICAR: Tecle [C] ou [c]\n- DECODIFICAR: Apenas [ENTER]\n\nOpção: ')

    if modo == 'c' or modo == 'C':
        c = cifra.criptografar(mensagem, chave)
        print('\nTexto:', c, '\n')
    else:
        dc = cifra.descriptografar(mensagem, chave)
        print('\nTexto:', dc, '\n')
   
    