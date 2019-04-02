#EX 01
print('Exemplo 01')

def mensagem():
    print("Programando em Python")

mensagem()


#EX 02
print('\nExemplo 02')

def mensagem(m):
    print(m)

mensagem("Olá")


#EX 03
print('\nExemplo 03')

def soma(a,b):
    print(a+b)

soma(10,20)


#EX 04
print('\nExemplo 04')

def maior(a, b):
    if (a > b):
        print(a, '>' ,b)  
    elif (a < b):
        print(b, '>' ,a)  
    else:
        print(a, '=' ,b)
        
maior(3,5)
maior(5,3)
maior(7,7)
maior(b=7,a=5)

#EX 05
print('\nExemplo 05')

def potencia(x,y=2):
    print(x**y)

potencia(2,5)
potencia(10)
#potencia(y=5) // ERRO // MODIFICA Y. MAS NÃO DECLARA X
#potencia(b=3, 7) // ERRO // MODIFICA Y, MAS NÃO DECLARA X
