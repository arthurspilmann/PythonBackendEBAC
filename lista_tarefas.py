#biblioteca das tarefas
tarefas = {}

#DEFININDO AS FUNÇOES DO CODIGO
# funçao para exibir o menu
def exibir_menu():
    print(
        "Menu: \n"
        "1 - Adicionar tarefa\n"
        "2 - Listar tarefas\n"
        "3 - Remover tarefas\n"
        "4 - Marcar tarefa como concluida\n"
        "5 - Sair\n"
    )

#função para adicionar tarefas no dicionario e verificar se já existem
def adicionar_tarefa(tarefas):
    nome = input("Qual o nome da tarefa a ser adicionada: ")
    if nome not in tarefas:
        tarefas[nome] = False
        print(f"Tarefa '{nome}' adicionada com sucesso!")
    else:
        print("Essa tarefa já existe.")

#função para mostrar as tarefas agendadas
def listar_tarefas(tarefas):
    #dicionário vazio é entendido como False
    # not tarefas com o o dicionário vazio é True
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return
    
    print("Lista de tarefas:")

    #percorre a lista "tarefas" com o operador "tarefa"
    #caso o correspondente seja True mostra o emoji correto.
    for tarefa in sorted(tarefas):
        if tarefas[tarefa] == True:
            print(f"✅ {tarefa}")
        else:
            print(f"❌ {tarefa}")

#função para remover uma tarefa do dicionário
def remover_tarefa(tarefas):
    nome  = input("Qual tarefa deseja remover?")

    #“Existe uma chave chamada nome dentro do dicionário tarefas?” Se existir → True
    if nome in tarefas:
        del tarefas[nome]
        print(f"Tarefa '{nome}' removida com sucesso!")
    else:
        print("Erro: Tarefa não encontrada.")

#função para marcar tarefa como concluída
def marcar_concluida(tarefas):
    nome  = input("Qual tarefa deseja marcar como concluída?")

    if nome in tarefas:
        tarefas[nome] = True
        print(f"Tarefa '{nome}' marcada como concluída!")
    else:
        print("Erro: Tarefa não encontrada.")

#FUNÇÃO PRINCIPAL
def main():

    while True:
        exibir_menu()
        escolha = input("Escolha uma opção\n")

        if escolha == '1':
            adicionar_tarefa(tarefas)
        elif escolha == '2':
            listar_tarefas(tarefas)
        elif escolha == '3':
            remover_tarefa(tarefas)
        elif escolha == '4':
            marcar_concluida(tarefas)
        elif escolha == '5':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")


    
if __name__ == "__main__":
    main()