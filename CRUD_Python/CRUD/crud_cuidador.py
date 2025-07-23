from Tabelas.cuidador import cuidador
from Database.functions import functions


db = functions(
    host="localhost",
    user="root",
    password="12345678",
    database="zoologicoo"
)

def criar_cuidador(nome, cpf, telefone):
    novo = cuidador(nome, cpf, telefone)
    db.criar("cuidador", novo)

def listar_cuidadores():
    cuidadores = db.listar("cuidador")
    for c in cuidadores:
        print(c)

def atualizar_cuidador(cpf, novo_nome, novo_telefone):
    campos = ["nome", "telefone"]
    valores = (novo_nome, novo_telefone)
    db.atualizar("cuidador", campos, valores, "cpf", cpf)

def remover_cuidador(cpf):
    db.remover("cuidador", "cpf", cpf)

def menu():
    while True:
        print("\n🐾 MENU - CUIDADOR")
        print("1. Criar cuidador")
        print("2. Listar cuidadores")
        print("3. Atualizar cuidador")
        print("4. Remover cuidador")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            cpf = input("CPF: ")
            telefone = input("Telefone: ")
            criar_cuidador(nome, cpf, telefone)

        elif opcao == "2":
            listar_cuidadores()

        elif opcao == "3":
            cpf = input("CPF do cuidador a atualizar: ")
            novo_nome = input("Novo nome: ")
            novo_telefone = input("Novo telefone: ")
            atualizar_cuidador(cpf, novo_nome, novo_telefone)

        elif opcao == "4":
            cpf = input("CPF do cuidador a remover: ")
            remover_cuidador(cpf)

        elif opcao == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()
