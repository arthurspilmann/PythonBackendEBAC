# recebe os números e se não for float cai no except
def recebe_numeros():
    while True:    
        try:
            num1 = float(input("Digite o primeiro número."))
            num2 = float(input("Digite o segundo número."))
            return num1, num2

        except ValueError:
            print("Erro: O valor não é um número.")
# a função verifica se o numero que está sendo dividido é 0
def calcular(opcao, num1, num2, operacoes):
    if opcao == "4":
        while True:
            try:
                return operacoes[opcao][1](num1, num2)
            except ZeroDivisionError:
                print("Erro: divisão por zero.")
                num2 = float(input("Digite outro número: "))
    return operacoes[opcao][1](num1, num2)

while True:
    num1, num2 = recebe_numeros()

    # biblioteca de operações com funções lambda e tuplas contendo os nomes das operações
    operacoes = {
        "1": ("Soma", lambda a, b: a + b),
        "2": ("Subtração", lambda a, b: a - b),
        "3": ("Multiplicação", lambda a, b: a * b),
        "4": ("Divisão", lambda a, b: a / b),
        "5": ("Potência", lambda a, b: a ** b),
    }

    #menu usando list comprehension
    menu = [f"{i} - {nome}" for i, (nome, funcao) in operacoes.items()]
    
    #print("\n".join(menu)) # o join adiciona a string que quebra alinha do menu para os itens da lista menu
    print("\n".join(menu))

    opcao = input("Digite a opção desejada.")

    # condições para verificar se a opção é válida
    if opcao not in operacoes:
        print("Erro: operação inválida.")
        continue
    
    resultado = calcular(opcao, num1, num2, operacoes)
    
    print("Resultado: ", resultado)

    continuar = input("Deseja realizar outra operação? (s/n)").lower()
    if continuar != "s":
        print("Encerrando...")
        break