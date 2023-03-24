import random

megasena = []
valor_sorteado = []
quantidade_sorteio = 6

while len(megasena) < quantidade_sorteio:
    sorteio = random.randint(1,60)
    if sorteio not in megasena:
        megasena.append(sorteio)

for valor in range(quantidade_sorteio):
    valor_sorteado.append(megasena[valor])

print("Os números da MEGA-SENA sorteados são: " + str(valor_sorteado))