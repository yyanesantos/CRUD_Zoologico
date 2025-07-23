from Tabelas.eventosEducativos import eventosEducativos
from Database.functions import functions

db = functions(
    host="localhost",
    user="root",
    password="12345678",
    database="zoologicoo"
)

def criar_evento(idEvento, nome, data, duracao):
    novo = eventosEducativos(idEvento, nome, data, duracao)
    db.criar("eventosEducativos", novo)

def listar_eventos():
    eventos = db.listar("eventosEducativos")
    for e in eventos:
        print(e)

def atualizar_evento(idEvento, nome, data, duracao):
    campos = ["nome", "data", "duracao"]
    valores = (nome, data, duracao)
    db.atualizar("eventosEducativos", campos, valores, "idEvento", idEvento)

def remover_evento(idEvento):
    db.remover("eventosEducativos", "idEvento", idEvento)

def menu():
    while True:
        print("\n MENU - EVENTOS EDUCATIVOS")
        print("1. Criar evento")
        print("2. Listar eventos")
        print("3. Atualizar evento")
        print("4. Remover evento")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            idEvento = input("ID do evento: ")
            nome = input("Nome: ")
            data = input("Data (AAAA-MM-DD): ")
            duracao = input("Duração (em horas): ")
            criar_evento(idEvento, nome, data, duracao)

        elif opcao == "2":
            listar_eventos()

        elif opcao == "3":
            idEvento = input("ID do evento a atualizar: ")
            nome = input("Novo nome: ")
            data = input("Nova data (AAAA-MM-DD): ")
            duracao = input("Nova duração (em horas): ")
            atualizar_evento(idEvento, nome, data, duracao)

        elif opcao == "4":
            idEvento = input("ID do evento a remover: ")
            remover_evento(idEvento)

        elif opcao == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()