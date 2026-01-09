
# dicionário op que relaciona os numeros (strings) com um Tuple (string e função lambda)
op = {
    "1": ("Soma", lambda a, b: a + b),
    "2": ("Subtração", lambda a, b: a - b),
    "3": ("Multiplicação", lambda a, b: a * b),
    "4": ("Divisão", lambda a, b: a / b),
    
}

# a lista menu recebe um for loop
menu = [f"{i} - {nome}" for i, (nome, funcao) in op.items()]

#adiciona um "\n" no fim de cada item da lista menu
print("\n".join(menu))

