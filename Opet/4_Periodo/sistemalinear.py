# Ricardo Baniski 1201800164

class SistemaLinear:
    def __init__(self, a11, a12, b1, a21, a22, b2):
        self.a11 = a11
        self.a12 = a12
        self.b1 = b1
        self.a21 = a21
        self.a22 = a22
        self.b2 = b2

    def imprime(self):
        print('\n{} x + {} y = {}'.format(self.a11, self.a12, self.b1))
        print('{} x + {} y = {}\n'.format(self.a21, self.a22, self.b2))

    def substituicao(self):
        y = (self.b2 / self.a22) / (1 - (self.a21 * self.a12) / (self.a11 * self.a22)) - ((self.a21 * self.b1) / (self.a11 * self.a22)) / (1 - (self.a21 * self.a12) / (self.a11 * self.a22))
        x = (self.b1 - self.a12 * y) / self.a11
        return x, y

    def cramer(self):
        d = self.a11 * self.a22 - self.a21 * self.a12
        dX = self.b1 * self.a22 - self.b2 * self.a12
        dY = self.a11 * self.b2 - self.b1 * self.a21
        x = dX / d
        y = dY / d
        return x, y


a11 = int(input('a11: '))   # 1
a12 = int(input('a12: '))   # 1
b1 = int(input('b1: '))     # 78
a21 = int(input('a21: '))   # 1
a22 = int(input('a22: '))   # 2
b2 = int(input('b2: '))     # 210

c = SistemaLinear(a11, a12, b1, a21, a22, b2)
c.imprime()
print('Cramer: ',c.cramer())
print('Substituição: ',c.substituicao())
