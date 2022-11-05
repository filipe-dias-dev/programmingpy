idade = 12
idades = [18, 20, 22, 21]

print(type(idades))
print(idades[2])
print(idades[0:3])
print(idades[1:])
print(idades[-1])
print(idades[-2])

lista = ['Filipe', 28, True, '18']

for elemento in lista:
  print(f'O elemento {elemento} é do tipo, ', type(elemento))