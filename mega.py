import random

num_sorteados = []

for i in range(6):

    num = random.randint(1, 60)
    if num not in num_sorteados:
        num_sorteados.append(num)

num_sorteados.sort()
print(num_sorteados)