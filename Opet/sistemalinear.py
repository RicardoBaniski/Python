class SistemaLinear:
    def __init__(self, a11, a12, b1, a21, a22, b2):
        self.a11 = a11
        self.a12 = a12
        self.b1 = b1
        self.a21 = a21
        self.a22 = a22
        self.b2 = b2

    def imprime(self):
        print('{} x + {} y = {}'.format(self.a11, self.a12, self.b1))
        print('{} x + {} y = {}'.format(self.a21, self.a22, self.b2))

    def subst1(self):
        return (self.b2 / (((self.b1 - self.a12) / self.a11) - self.a22))


a11 = int(input('a11: '))
a12 = int(input('a12: '))
b1 = int(input('b1: '))
a21 = int(input('a21: '))
a22 = int(input('a22: '))
b2 = int(input('b2: '))

equacoes = SistemaLinear(a11, a12, b1, a21, a22, b2)
print(equacoes.imprime())
print(equacoes.subst1())
