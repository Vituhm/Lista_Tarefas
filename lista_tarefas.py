tarefas = []

#adicionar tarefa 
def adicionar_tarefa():  
    tarefa = input("Digite a tarefa a ser adicionada: ")
    tarefas.append(tarefa)
    print("Tarefa adicionada!")

#marcar concluída
def marcar_concluida():
    listar_tarefas()
    indice = int(input("Digite o número da tarefa concluída: "))
    if 0 <= indice < len(tarefas):
        tarefas[indice] = f"[Concluída] {tarefas[indice]}"
        print("Tarefa marcada como concluída!")
    else:
        print("Valor inválido!")

#listar tarefas
def listar_tarefas():
    print("\nLista de Tarefas:")
    for i, tarefa in enumerate(tarefas):
        print(f"{i}: {tarefa}")

#excluir tarefa
def excluir_tarefa():
    listar_tarefas()
    indice = int(input("Digite o índice da tarefa a ser excluída: "))
    if 0 <= indice < len(tarefas):
        tarefas.pop(indice)
        print("Tarefa excluída!")
        listar_tarefas()
    else:
        print("Índice inválido!")

#limpar a lista
def limpar_lista():
    tarefas.clear()
    print("Lista de tarefas exluída!")

#loop principal
while True:
    print("____________________________________")
    print("______LISTA__DE__TAREFAS____________")
    print("-- Selecione uma opção --")
    print("1) Adicionar uma tarefa")
    print("2) Marcar tarefa 'Concluída'")
    print("3) Listar tarefas")
    print("4) Excluir uma tarefa")
    print("5) Limpar lista de tarefas")
    print("6) Sair")
    print("____________________________________")

    op=input("Escolha uma opção: ")

    match op:
        case "1":
            adicionar_tarefa()
        case "2":
            marcar_concluida()
        case "3":
            listar_tarefas()
        case "4":
            excluir_tarefa()
        case "5":
            limpar_lista()
        case "6":
            print("Encerrando lista..")
            break
        case _:
            print("Opção inválida. Tente novamente.")
