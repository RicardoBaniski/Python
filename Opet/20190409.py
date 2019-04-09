class MinhaClasse:
    pass    #Palavra reservada
            #Segue em Frente
            #Com o Programa

#Atributos:


class Quadrado:
    lado = 5

q1 = Quadrado()
q2 = Quadrado()
q2.lado = 10
print(q1.lado)
print(q2.lado)


class Produto:
    preco = 15.00

p1 = Produto()
p1.nome = 'Batata'
print(p1.nome)
p2 = Produto()
print(Produto.preco)
print(p2.preco)
Produto.categoria = 'Legume'
print(p2.categoria)
print(Produto.nome)

#Métodos:


class Retangulo:
    base = 15
    altura = 10
    def area(self):
        return self.base * self.altura
    
r1 = Retangulo()
r2 = Retangulo()
r2.base = 20
r2.altura = 30
print(r1.area())
print(r2.area())
print(Retangulo.area(r2))

