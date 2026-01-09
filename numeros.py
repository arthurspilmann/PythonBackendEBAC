# Escreva um programa que receba três numeros e exiba o segundo maior numero.

lista_numero = []

lista_numero.append(float(input("Digite o primeiro numero: ")))

lista_numero.append(float(input("Digite o segundo numero: ")))

lista_numero.append(float(input("Digite o terceiro numero: ")))

for i in range(3): # 3 é porque a lista tem apenas três valores
    for j in range(i + 1, 3):  #range(inicio, fim, passo), i + 1 evita que compare o primeiro valor com ele mesmo
        if lista_numero[j] > lista_numero[i]:
            lista_numero[i], lista_numero[j] = lista_numero[j], lista_numero[i]


print(lista_numero[1])
