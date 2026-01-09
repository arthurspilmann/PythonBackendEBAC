lista_palavras = []
x = True

while x == True:
    lista_palavras.append(input("Digite uma palavra para a lista: "))

    print(lista_palavras)

    continua = input("Deseja adicionar outra palavra? (s/n) ")

    if continua == "s":
        continue
    else:
        lista_em_ordem = sorted(lista_palavras)
        print(f"A lista me ordem alfabética é: {lista_em_ordem}")
        x = False
print("Fim...")