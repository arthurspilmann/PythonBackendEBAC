'''Dado uma lista de numeros, pegar apenas aqueles que o quadrado é impar'''

numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
quadrados = []

'''
for numero in numeros:
    quadrado = numero**2
    if quadrado%2 != 0:
        quadrados.append(quadrado)
    else:
        quadrados.append("par")

print(numeros)
print(quadrados)
'''

quadrados_impares = [elemento**2 for elemento in numeros if elemento%2 != 0]

# Crie uma lista com elemento**2 para cada elemento em numeros se elemento for impar

'''
[elemento**2               # o que será colocado na lista
 for elemento in numeros   # de onde vem cada valor
 if elemento % 2 != 0]     # condição (filtro)
'''


print(quadrados_impares)