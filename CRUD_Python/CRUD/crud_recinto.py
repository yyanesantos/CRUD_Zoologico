from Tabelas.recinto import recinto
from Database.functions import functions

db = functions(
    host="localhost",
    user="root",
    password="12345678",
    database="zoologicoo"
)

def criar_recinto(idRecinto, local, capacidadeMaxima):
    novo = recinto(idRecinto, local, capacidadeMaxima)
    db.criar("recinto", novo)

def listar_recintos():
    recintos = db.listar("recinto")
    for r in recintos:
        print(r)

def atualizar_recinto(idRecinto, novo_local, nova_capacidade):
    campos = ["local", "capacidadeMaxima"]
    valores = (novo_local, nova_capacidade)
    db.atualizar("recinto", campos, valores, "idRecinto", idRecinto)

def remover_recinto(idRecinto):
    db.remover("recinto", "idRecinto", idRecinto)

def menu():
    while True:
        print("\n🏠 MENU - RECINTO")
        print("1. Criar recinto")
        print("2. Listar recintos")
        print("3. Atualizar recinto")
        print("4. Remover recinto")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            idRecinto = int(input("ID do recinto: "))
            local = input("Local do recinto: ")
            capacidadeMaxima = int(input("Capacidade máxima: "))
            criar_recinto(idRecinto, local, capacidadeMaxima)

        elif opcao == "2":
            listar_recintos()

        elif opcao == "3":
            idRecinto = int(input("ID do recinto a atualizar: "))
            novo_local = input("Novo local: ")
            nova_capacidade = int(input("Nova capacidade máxima: "))
            atualizar_recinto(idRecinto, novo_local, nova_capacidade)

        elif opcao == "4":
            idRecinto = int(input("ID do recinto a remover: "))
            remover_recinto(idRecinto)

        elif opcao == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()