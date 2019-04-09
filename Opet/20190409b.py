print('TRIANGULO_02')


class Triangulo:
    def __init__(self, b=10, h=10):
        self.b = b
        self.h = h

    def area(self):
        return(self.b * self.h) / 2


t1 = Triangulo(20, 20)  # b, h
t2 = Triangulo(15)      # b
t3 = Triangulo(h=30)    # h
t4 = Triangulo()        # NENHUM
print(t1.area())
print(t2.area())
print(t3.area())
print(t4.area())

print('\nEMPRESTIMO')


class Emprestimo:
    def __init__(self, v=10000):
        self.v = v

    def juros(self, taxa):
        return self.v * (taxa / 100)


e1 = Emprestimo()
e2 = Emprestimo(500)
print(e1.juros(20))  # 2000
print(e2.juros(10))  # 50.0


class Emprestimo2:
    def __init__(self, v=10000):
        self.v = v

    def juros(self, taxa):
        return self.v*(taxa/100)

    def total(self, taxa):
        return self.v + self.juros(taxa)


e1 = Emprestimo2()
print(e1.juros(10))
print(e1.total(10))