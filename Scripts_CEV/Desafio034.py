salario = int(input('Qual o salário: '))

aumento = 0

if salario > 1250:
    aumento = salario * (10/100)
else:
    aumento = salario * (15/100)
print('Você receberá um aumento de R${:.2f}, e passará a receber R${:.2f}'.format(
    aumento, salario+aumento))
