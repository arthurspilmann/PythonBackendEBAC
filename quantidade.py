# dado um array de numero inteiros, retornar quantos deles possuem um numero par de digitos

num = [64657, 892348, 46452, 1634, 8956, 135, 78346, 12313534, 56464, 12336]    #lista de numeros
cont = 0    # contador para saber quantos são pares

for i in num:   #percorre a lista num com a variavel i
    q = len(str(i))     #transforma i em string e pega a quantidade de letras na variavel q

    if q % 2 == 0:  #se o resto da divisão de q por 2 for 0, q é par
        cont += 1

print(f"A quantidade de números com números pares de digitos é: {cont}")