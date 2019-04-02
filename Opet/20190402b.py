print('Exemplo 06')

def soma(*args):
    if args:
        s = 0
        for i in args:
            s += i
            print(s)
    else:
        print('Vazio')

soma()
soma(5)
soma(1, 2, 3, 4, 5)


print('\nExemplo 07')

def conexao(**args):
    con_param = {'host':args.get('host','127.0.0.1'),
               'port':args.get('port',8000),
               'user':args.get('user',''),
               'pwd':args.get('pwd','123'),
                 }
    print(con_param)
               
conexao()
conexao(host = '192.168.0.1')
conexao(port = 9000, user = 'admin', pwd = '@dmin')


print('\nExemplo 08')

def funcao(x, *y, **z):
    print(x)
    print(y)
    print(z)

#funcao() // ERRO
funcao(5)
funcao(5, 10)
funcao(5, 10, 15, k = 20)
