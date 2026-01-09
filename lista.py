#list = []
#for i in range(1, 10, 2):
#    list.append(i)
#print(list)'''

#list = [i + i/2 for i in range(3)]
#print(list)

#operacoes = ["Soma", "Subtração", "Multiplicação", "Divisão", "Sair"]

#menu = [f"{i + 1} - {operacoes[i]}" for i in range(len(operacoes))]

#print("\n".join(menu))

"""nome = "Arthur"

letras = list(nome)
print(letras)

letras.append("O")

print(letras)

letras.pop(-1)

print(letras)

print(tuple(nome))

del tuple(nome)[0]
print(tuple(nome)[0])"""

'''numero = 5

nome = ["João", "Tonho", "Jean", "Arthur"]

lista = [5, 6, 10, 54]


enumerate(lista)

for l, n in zip(lista, nome):
    print(f"O nome {n} corresponde ao número {l}")
'''
'''
listas = {
    5: "João",
    6: "Tonho",
    10: "Jean",
    54: "Arthur"
}

listas.items()

m = [f"O número {k} está relacionado ao nome {v}" for k, v in listas.items()]
print("\n".join(m))'''

'''def pin_extractor(poem):
    secret_code = ''
    
poem = """Stars and the moon
shine in the sky
white and bright
until the end of the night"""

pin_extractor(poem)

lines = poem.split("\n")

#print(lines[0].split())

for line in lines:
    words = line.split()
    print(words)

#print(lines)'''


products = {
    'Laptop': 990,
    'Smartphone': 600,
    'Tablet': 250,
    'Headphones': 70,
}

for product, price in products.items():
    products[product] = round(price*0.8)
    

print(products)


for index, product in enumerate(products.items(), 1): # enumerate retorna um tuple que é armazenado no index e product
    print(index, product)
