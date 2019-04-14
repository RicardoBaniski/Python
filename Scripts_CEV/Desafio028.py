import random

maquina = random.randint(0, 5)

usuario = int(input("Adivinhe o numero: "))

print('VENCEU' if maquina == usuario else 'PERDEU')