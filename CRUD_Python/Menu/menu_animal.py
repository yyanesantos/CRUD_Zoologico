from CRUD.crud_animal import animalCrud

def menuAnimal():
    print("eae")
    crud = animalCrud(host="localhost", user="root", password="12345678", database="zoologicoo")
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
            recinto = input("Recinto (ID): ")
            crud.criar_animal(idAnimal, nome, dataNascimento, sexo, especie, recinto)

        elif opcao == "2":
            crud.listar_animais()

        elif opcao == "3":
            idAnimal = input("ID do animal a atualizar: ")
            nome = input("Novo nome: ")
            dataNascimento = input("Nova data de nascimento (AAAA-MM-DD): ")
            sexo = input("Novo sexo (M/F): ")
            especie = input("Nova espécie (nome científico): ")
            recinto = input("Novo recinto: ")
            crud.atualizar_animal(idAnimal, nome, dataNascimento, sexo, especie, recinto)

        elif opcao == "4":
            idAnimal = input("ID do animal a remover: ")
            crud.remover_animal(idAnimal)

        elif opcao == "0":
            break

        else:
            print("Opção inválida.")

    #if __name__ == "__main__":
     #   menuAnimal()