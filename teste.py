nome = "Arhur 123"

lista = []

for i in nome:
    if i.isalpha():
        lista.append("str")
    elif i.isdigit():
        lista.append("int")

print(lista)