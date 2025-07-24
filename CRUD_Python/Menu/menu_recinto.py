from CRUD.crud_recinto import recintoCrud

def menuRecinto():
    crud = recintoCrud(host="localhost", user="root", password="12345678", database="zoologicoo")
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
            crud.criar_recinto(idRecinto, local, capacidadeMaxima)

        elif opcao == "2":
            crud.listar_recintos()

        elif opcao == "3":
            idRecinto = int(input("ID do recinto a atualizar: "))
            novo_local = input("Novo local: ")
            nova_capacidade = int(input("Nova capacidade máxima: "))
            crud.atualizar_recinto(idRecinto, novo_local, nova_capacidade)

        elif opcao == "4":
            idRecinto = int(input("ID do recinto a remover: "))
            crud.remover_recinto(idRecinto)

        elif opcao == "0":
            break

        else:
            print("Opção inválida.")

    if __name__ == "__main__":
        menuRecinto()