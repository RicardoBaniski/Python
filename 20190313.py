#PYTHON3
#https://repl.it/languages/python3

str1 = 'Primeira String'
print(str1)

str2 = "Segunda String"
print(str2)

str3 = 'Primeira Linha\nSegunda Linha'

print(str3)

str4 = '''Linha 1
Linha 2
...
Linha N
'''
print(str4)

print(len(str2))

print(str1[0])
print(str1[:3])
print(str1[3:8])

palavras = str1.split(" ")
print(palavras)

palavras = str.split(str1)
print(palavras)

musica = '''Faster than a bullet
Terrifying scream
Enraged and full of anger
He's half man and half machine
Rides the Metal Monster
Breathing smoke and fire
Closing in with vengeance soaring high
He is the Painkiller
This is the Painkiller
Planets devastated
Mankind's on its knees
A saviour comes from out the skies
In answer to their pleas
Through boiling clouds of thunder
Blasting bolts of steel
Evils going under deadly wheels
He is the Painkiller
This is the Painkiller
Faster than a laser bullet
Louder than an atom bomb
Chromium plated boiling metal
Brighter than a thousand suns
Flying high on rapture
Stronger free and brave
Nevermore encaptured
They've been brought back from the grave
With mankind ressurrected
Forever to survive
Returns from Armageddon to the skies
He is the Painkiller
This is the Painkiller
Wings of steel Painkiller
Deadly wheels Painkiller
He is the painkiller
This is the painkiller
Pain
Pain
Killer
Killer
Can't stop the Painkiller
Pain'''

palavras = str.split(musica)
print(palavras)

print(len(musica))
print(len(palavras))

print(musica[0])
print(palavras[0])

print(musica[-1])
print(palavras[-1])