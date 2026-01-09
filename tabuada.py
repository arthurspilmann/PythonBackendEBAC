numero = int(input("Digite um número."))
tabuada = []

for i in range(0, 100):
    resultado = numero*(i+1)
    tabuada.append(resultado)

print(f"TABUADA DO {numero}")

for i in range(0, 100):
    print(f"{i+1} x {numero} = {tabuada[i]}")