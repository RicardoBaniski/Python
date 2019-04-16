from datetime import date

hoje = date.today()

nascimento = int(input('Data de nascimento: '))

idade = hoje.year-nascimento

if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JUNIOR')
elif idade <= 20:
    print('SÊNIOR')
else:
    print('MASTER')
