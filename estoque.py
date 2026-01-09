#Funções

# Exibe o munu com as opçoes disponíveis
def exibir_menu():
    print(
        "\nMENU\n"
        "1 - Adicionar produto\n"
        "2 - Listar produtos\n"
        "3 - Remover produto\n"
        "4 - Atualizar quantidade\n"
        "5 - Sair"
    )

'''Adiciona u
asdasdasdasm produto '''
def adicionar(dicionario):
    novo_produto = input("Qual produto deseja adicionar?")

    if novo_produto in dicionario:
        print("Produto já existe.")
        return

    quant = int(input("Qual a quantidade desse produto?"))
    preço = float(input("Qual o preço desse produto?"))

    dicionario[novo_produto] = {
        "quantidade": quant,
        "preço": preço
    }

    print("Produto adicionado com sucesso!")

# Mostra os produtos em forma de tabela
def listar(dicionario):
    print("Produtos cadastrados:")

    for produto, info in sorted(dicionario.items(), key=lambda item: item[0]):
        print(f"{produto}: {info['quantidade']} - R$ {info['preço']:.2f}")
   

# Remove um produto
def remover(dicionario):
    produto_remov = input("Qual produto deseja remover? ")

    if produto_remov in dicionario:
        dicionario.pop(produto_remov)
        print(f"Produto '{produto_remov}' removido com sucesso!")
    else:
        print("Erro: Produto não encontrado.")

# Atualiza a quantidade disponivel de algum produto
def atualizar(dicionario):
    atualiza = input("Qual item deseja atualizar? ")

    if atualiza not in dicionario:
        print("Produto não encontrado.")
    else:
        nova_quant = int(input("Qual a nova quantidade? "))
        dicionario[atualiza]["quantidade"] = nova_quant
        print("Quantidade atualizada!")
        

def main():

    produtos = {
        "Maça" : {
            "quantidade": 3,
            "preço": 1.10
        },
        "Banana" : {
            "quantidade": 5,
            "preço": 0.75
        },
        "Leite" : {
            "quantidade": 12,
            "preço": 4.30
        },
        "Farinha" : {
            "quantidade": 45,
            "preço": 5.85
        }
    }

    while True:
        exibir_menu()
        escolha = input("Qual opção deseja? ")

        if escolha == '1':
            adicionar(produtos)
        
        elif escolha == '2':
            listar(produtos)

        elif escolha == '3':
            remover(produtos)

        elif escolha == '4':
            atualizar(produtos)

        elif escolha == '5':
            print("Fechando a tabela de produtos...")
            break
        else:
            print("Opção inválida.\nEscolha uma das opções válidas.")


    return

if __name__ == "__main__":
    main()

