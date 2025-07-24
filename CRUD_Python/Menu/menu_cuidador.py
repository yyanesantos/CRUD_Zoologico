from CRUD.crud_cuidador import cuidadorCrud

def menuCuidador():
    crud = cuidadorCrud(host="localhost", user="root", password="12345678", database="zoologicoo")
    while True:
        print("\n🐾 MENU - CUIDADOR")
        print("1. Criar cuidador")
        print("2. Listar cuidadores")
        print("3. Atualizar cuidador")
        print("4. Remover cuidador")
        print("5. Adicionar animal ao cuidador")
        print("6. Remover animal de cuidador")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            cpf = input("CPF: ")
            telefone = input("Telefone: ")
            if crud.criar_cuidador(nome, cpf, telefone):
                while True:
                    idAnimal = input("ID do animal para associar (ou Enter para sair): ").strip()
                    if idAnimal == "":
                        break
                    crud.db.adicionar_dualTabela("cuidadorAnimal", ["cpfCuidador", "idAnimal"], (cpf, idAnimal))

        elif opcao == "2":
            crud.listar_cuidadores()

        elif opcao == "3":
            cpf = input("CPF do cuidador a atualizar: ")
            novo_nome = input("Novo nome: ")
            novo_telefone = input("Novo telefone: ")
            

        elif opcao == "4":
            cpf = input("CPF do cuidador a remover: ")
            crud.remover_cuidador(cpf)

        elif opcao == "5":
            cpf = input("CPF do cuidador para se adicionar o animal: ")
            idAnimal = input("ID do animal a ser adicionado aos cuidados do cuidador: ")
            crud.adicionar_animal_ao_cuidador(cpf, idAnimal)

        elif opcao == "6":
            cpf = input("CPF do cuidador para se remover o animal: ")
            idAnimal = input("ID do animal a ser removido dos cuidados do cuidador: ")
            crud.remover_animal_de_cuidador(cpf, idAnimal)

        elif opcao == "0":
            break

        else:
            print("Opção inválida.")

    if __name__ == "__main__":
        menuCuidador()
