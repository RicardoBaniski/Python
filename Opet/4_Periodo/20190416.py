class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def getPessoa(self):
        return self.nome+''+str(self.idade)


class Funcionario(Pessoa):
    def __init__(self, nome, idade, salario):
        Pessoa.__init__(self, nome, idade)
        self.salario = salario

    def getFuncionario(self):
        return self.getPessoa()+''+str(self.salario)


p1 = Pessoa('Paulo', 23)
f1 = Funcionario('Maria', 35, 3500.00)
print(p1.getPessoa())           # Paulo 23
print(f1.getFuncionario())      # Maria 35v 3500.00
print(f1.getPessoa())           # Maria 35
