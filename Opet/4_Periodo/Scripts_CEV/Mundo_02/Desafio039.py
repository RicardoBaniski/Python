from datetime import date

hoje = date.today()
#print(hoje.year)

nasc = int(input('Ano de nascimento: '))

idade = hoje.year - nasc

if idade == 18:
    print('Você precisa se alistar imediatamente!')
elif idade < 18:
    print('Ainda falta(m) {} ano(s) para você se alistar!'.format(18 - idade))
else:
    print('Já passou seu período de alistamento\nProcure a Junta Militar mais próxima!')
