from Tabelas.animal import animal
from Database.functions import functions

db = functions(
    host="localhost",
    user="root",
    password="12345678",
    database="zoologicoo"
)

def criar_animal(idAnimal, nome, dataNascimento, sexo, especie, recinto):
    novo = animal(idAnimal, nome, dataNascimento, sexo, especie, recinto)
    db.criar("animal", novo)

def listar_animais():
    animais = db.listar("animal")
    for a in animais:
        print(a)

def atualizar_animal(idAnimal, nome, dataNascimento, sexo, especie, recinto):
    campos = ["nome", "dataNascimento", "sexo", "especie", "recinto"]
    valores = (nome, dataNascimento, sexo, especie, recinto)
    db.atualizar("animal", campos, valores, "idAnimal", idAnimal)

def remover_animal(idAnimal):
    db.remover("animal", "idAnimal", idAnimal)

def menu():
    while True:
        print("\n MENU - ANIMAIS")
        print("1. Criar animal")
        print("2. Listar animais")
        print("3. Atualizar animal")
        print("4. Remover animal")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            idAnimal = input("ID do animal: ")
            nome = input("Nome: ")
            dataNascimento = input("Data de nascimento (AAAA-MM-DD): ")
            sexo = input("Sexo (M/F): ")
            especie = input("Espécie (nome científico): ")
            recinto = input("Recinto: ")
            criar_animal(idAnimal, nome, dataNascimento, sexo, especie, recinto)

        elif opcao == "2":
            listar_animais()

        elif opcao == "3":
            idAnimal = input("ID do animal a atualizar: ")
            nome = input("Novo nome: ")
            dataNascimento = input("Nova data de nascimento (AAAA-MM-DD): ")
            sexo = input("Novo sexo (M/F): ")
            especie = input("Nova espécie (nome científico): ")
            recinto = input("Novo recinto: ")
            atualizar_animal(idAnimal, nome, dataNascimento, sexo, especie, recinto)

        elif opcao == "4":
            idAnimal = input("ID do animal a remover: ")
            remover_animal(idAnimal)

        elif opcao == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()