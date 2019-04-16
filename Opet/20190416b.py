# SOBRECARGA DE MÉTODO
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return self.nome+''+str(self.idade)


class Funcionario(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario

    def __str__(self):
        return super().__str__()+''+str(self.salario)


f1 = Funcionario('Pablo', 30, 2700.00)
f2 = Funcionario('Ana', 23, 3000.00)
p1 = Pessoa('Carlos', 37)

print(f1)       #
print(f2)       #
print(p1)       #
