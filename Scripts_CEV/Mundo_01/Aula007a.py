n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print('soma {}, \nmultiplicação {}, \ndivisão {:.3f}, \ndivisão sobra {} \ne potencia {}'.format(s,m,d,di,e))