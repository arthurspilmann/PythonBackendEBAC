#Funções
# Exibe o munu com as opçoes disponíveis
def exibir_menu():
    print(
        "\nMENU\n"
        "1 - Adicionar livro\n"
        "2 - Listar livros\n"
        "3 - Remover livro\n"
        "4 - Atualizar quantidade de livros\n"
        "5 - Registrar empréstimo\n"
        "6 - Exibir histórico de empréstimos\n"
        "7 - Sair"
    )

# adiciona um livro
def adicionar(dicionario):
    novo_livro = input("Qual livro deseja adicionar?")

    if novo_livro in dicionario:
        print("Livro já existe.")
        return

    autor = input("Qual o nome do autor?")
    quant = int(input("Qual a quantidade de exemplares?"))
    

    dicionario[novo_livro] = {
        "autor": autor,
        "quantidade": quant
    }

    print("Livro adicionado com sucesso!")

# Mostra os livros em forma de tabela
def listar(dicionario):
    print("Livros cadastrados:")

    # dicionario.items() retorna pares (chave, valor)
    # key=lambda item: item[0] indica que a ordenação será feita usando a chave (nome do livro)
    # key é parametro da função sorted
    for livro, info in sorted(dicionario.items(), key=lambda item: item[0]):
        print(f"{livro}; Autor: {info['autor']}; Exemplares: {info['quantidade']}")
   

# Remove um produto
def remover(dicionario):
    livro_remov = input("Qual livro deseja remover? ")

    if livro_remov in dicionario:
        dicionario.pop(livro_remov)
        print(f"Livro '{livro_remov}' removido com sucesso!")
    else:
        print("Erro: Livro não encontrado.")

# Atualiza a quantidade disponivel de algum livro
def atualizar(dicionario):
    atualiza = input("Qual livro deseja atualizar? ")

    if atualiza not in dicionario:
        print("Livro não encontrado.")
    else:
        nova_quant = int(input("Qual a nova quantidade? "))
        dicionario[atualiza]["quantidade"] = nova_quant
        print("Quantidade atualizada!")
        
# Registra o emprestímo de alguma livro. (X exemplares emprestados)

def registrar_emprestimo(dicionario, emprestimos):
    emp = input("Qual livro deseja emprestar?")

    if emp not in dicionario:
        print("Livro não encontrado na biblioteca.")
        return
    
    quant = int(input(f"Exitem {dicionario[emp]["quantidade"]} disponíveis. Quantos deseja emprestar?"))
    
    if quant > dicionario[emp]["quantidade"]:
        print(f"Quantidade total indisponível. Só existem {dicionario[emp]['quantidade']} na nossa biblioteca.")
        return
     
    print(f"{quant} exemplares de {emp} emprestados com sucesso!")
    dicionario[emp]["quantidade"] -= quant
    
    emprestimos.append([emp, quant])
    return

def historico_emprestimos(emprestimos):
    if not emprestimos:
        print("Nenhum empréstimo realizado.")
        return

    for titulo, quant in emprestimos:
        print (f"{quant} exemplares emprestados de {titulo}")
    return
 

def main():
    # dicionario com os livros
    catalogo = {
        "Cem anos de solidão" : {
            "autor": "Gabriel Garcia Marquez",
            "quantidade": 3
        },
        "O filho de mil homens" : {
            "autor": "Valter Hugo Mãe",
            "quantidade": 2
        },
        "O Hobbit" : {
            "autor": "J.R.R. Tolkien",
            "quantidade": 1
        },
    }

    # lista para guardar quais os livros estão esprestados
    emprestimos = []

    while True:
        exibir_menu()
        escolha = input("Qual opção deseja? ")

        if escolha == '1':
            adicionar(catalogo)
        
        elif escolha == '2':
            listar(catalogo)

        elif escolha == '3':
            remover(catalogo)

        elif escolha == '4':
            atualizar(catalogo)

        elif escolha == '5':
            registrar_emprestimo(catalogo, emprestimos)

        elif escolha == '6':
            historico_emprestimos(emprestimos)
        
        elif escolha == '7':
            print("Saindo do sistema...")
            break
            
        else:
            print("Opção inválida.\nEscolha uma das opções válidas.")


    return

if __name__ == "__main__":
    main()

