# SOBRECARGA DE MÉTODO
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __lt__(self, other):
        return self.idade < other.idade


class Funcionario(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario

    def __add__(self, other):
        return self.salario + other.salario


f1 = Funcionario('A', 37, 1500.00)
f2 = Funcionario('B', 22, 1200.00)
f3 = Funcionario('C', 40, 3000.00)

#print(f1 + f2 + f3)
lista = [f1, f2, f3]

[print(x.nome) for x in lista]

lista.sort()

[print(x.nome) for x in lista]
