import random
#sorteia numeros aleatorios de 1 a 60 e exibe.
print('lista 6 numeros de 1 a 60')
lista = []

while len(lista) < 6:
    numero = random.randint(1,60)
    if numero not in lista:
        lista.append(numero)

print('os numeros sorteados são:\n')
print(lista)