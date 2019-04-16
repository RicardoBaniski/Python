valorCasa = int(input('Qual o vbalor da casa? '))
salario = int(input('Qual o salário do comprador? '))
parcelas = int(input('Em quantas parcelas pretende financiar? '))

valorParcela = valorCasa/parcelas

limiteMensal = salario*0.30

if valorParcela > limiteMensal:
    print('Empréstimo negado!\nO valor da parcela não pode exceder o valor de R${:.2f}'.format(limiteMensal))
else:
    print('Serão {} parcelas de R${:.2f}'.format(parcelas, valorParcela))
