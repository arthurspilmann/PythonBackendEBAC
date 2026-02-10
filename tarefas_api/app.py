from fastapi import FastAPI

app = FastAPI()

tarefas = []

''' Cada tarefa será um dicionário, assim:
{
    "nome": "Estudar FastAPI",
    "descricao": "Aprender rotas e métodos HTTP",
    "concluida": False
}
'''

from fastapi import Body
# POST é a rota que recebe dados no corpo da requisição
# @ é o decorator que expande a função
@app.post("/tarefas")
def adicionar_tarefas(dados: dict = Body(...)):
    tarefa = {
        "nome": dados["nome"],
        "descricao": dados["descricao"],
        "concluida": False
    }
    tarefas.append(tarefa)
    return {"mensagem": "Tarefa adicionada com sucesso", "tarefa": tarefa}

# rota para listas as tarefas cadastradas
@app.get("/tarefas")
def listas_tarefas():
    return tarefas

# marcar a tarefa como concluída
@app.put("/tarefas/{nome}")
def concluir_tarefa(nome: str):
    for tarefa in tarefas:
        if tarefa["nome"] == nome:
            tarefa["concluida"] = True
            return {"mensagem": "Tarefa marcada como concluída", "tarefa": tarefa}
        
    return {"erro": "Tarefa não encontrada"}

# deletar tarefa
#.remove é um método de listas do python
@app.delete("/tarefas/{nome}")
def remover_tarefa(nome: str):
    for tarefa in tarefas:
        if tarefa["nome"] == nome:
            tarefas.remove(tarefa)
            return {"mensagem": "Tarefa removida com sucesso"}
        
    return {"erro": "Tarefa não encontrada"}