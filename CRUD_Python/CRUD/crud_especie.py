from Tabelas.especie import especie
from Database.functions import functions

db = functions(
    host="localhost",
    user="root",
    password="12345678",
    database="zoologicoo"
)

def criar_especie(nomeCientifico, nomeComum, habitatNatural):
    nova = especie(nomeCientifico, nomeComum, habitatNatural)
    db.criar("especie", nova)

def listar_especies():
    especies = db.listar("especie")
    for e in especies:
        print(e)

def atualizar_especie(nomeCientifico, novo_nomeComum, novo_habitat):
    campos = ["nomeComum", "habitatNatural"]
    valores = (novo_nomeComum, novo_habitat)
    db.atualizar("especie", campos, valores, "nomeCientifico", nomeCientifico)

def remover_especie(nomeCientifico):
    db.remover("especie", "nomeCientifico", nomeCientifico)

def menu():
    while True:
        print("\n🐾 MENU - ESPÉCIE")
        print("1. Criar espécie")
        print("2. Listar espécies")
        print("3. Atualizar espécie")
        print("4. Remover espécie")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nomeCientifico = input("Nome científico: ")
            nomeComum = input("Nome comum: ")
            habitatNatural = input("Habitat natural: ")
            criar_especie(nomeCientifico, nomeComum, habitatNatural)

        elif opcao == "2":
            listar_especies()

        elif opcao == "3":
            nomeCientifico = input("Nome científico da espécie a atualizar: ")
            novo_nomeComum = input("Novo nome comum: ")
            novo_habitat = input("Novo habitat natural: ")
            atualizar_especie(nomeCientifico, novo_nomeComum, novo_habitat)

        elif opcao == "4":
            nomeCientifico = input("Nome científico da espécie a remover: ")
            remover_especie(nomeCientifico)

        elif opcao == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()