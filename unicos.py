#Receba um array de numero inteiros e some cada um deles que aparece apenas uma vez

"""num = [1,1,2,5,4,6,8,4,4,6,6,3]     #lista de valores
cont = 0    #contador para saber quando aparecem apenas uma vez (não é necessário mas é legal saber)
soma = 0    #variável para armazenar a soma

for i in num:   #loop para percorrer cada numero da lista na variavel i
    if num.count(i) == 1:   #num.count(i) conta quantas vezes cada numero i aparece na lista e se for igual a 1 soma
        soma += i
        cont += 1
"""
soma = 0
cont = 0

num = [1,1,2,5,4,6,8,4,4,6,6,3]

dicionario = {}

for i in num:
    dicionario[i] = num.count(i)

print(dicionario.items())

for chave, valor in dicionario.items():
    print(chave, valor)

#print(f"Existem exatamente {cont} número que só aparecem uma vez na lista e a soma deles é {soma}.")