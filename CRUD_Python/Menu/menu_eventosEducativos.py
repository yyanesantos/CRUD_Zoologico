from CRUD.crud_eventosEducativos import eventosEducativosCrud

def menuEventosEducativos():
    crud = eventosEducativosCrud(host="localhost", user="root", password="12345678", database="zoologicoo")
    while True:
        print("\n MENU - EVENTOS EDUCATIVOS")
        print("1. Criar evento")
        print("2. Listar eventos")
        print("3. Atualizar evento")
        print("4. Remover evento")
        print("5. Adicionar animal à evento")
        print("6. Remover animal de evento")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            idEvento = input("ID do evento: ")
            nome = input("Nome: ")
            data = input("Data (AAAA-MM-DD): ")
            duracao = input("Duração (HHMMSS): ")
            if crud.criar_evento(idEvento, nome, data, duracao):
                while True:
                    idAnimal = input("ID do animal para associar ao evento (ou enter para sair): ").strip()
                    if idAnimal == "":
                        break
                    crud.db.adicionar_dualTabela("eventosAnimais", ["idEvento", "idAnimal"], (idEvento, idAnimal))

        elif opcao == "2":
            crud.listar_eventos()

        elif opcao == "3":
            idEvento = input("ID do evento a atualizar: ")
            nome = input("Novo nome: ")
            data = input("Nova data (AAAA-MM-DD): ")
            duracao = input("Nova duração (em horas): ")
            crud.atualizar_evento(idEvento, nome, data, duracao)

        elif opcao == "4":
            idEvento = input("ID do evento a remover: ")
            crud.remover_evento(idEvento)

        elif opcao == "5":
            idEvento = input("ID do evento a ser adicionado o animal: ")
            idAnimal = input("ID do animal a ser adicionado no evento: ")
            crud.adicionar_animal_de_evento(idEvento, idAnimal)

        elif opcao == "6":
            idEvento = input("ID do evento a ser removido o animal: ")
            idAnimal = input("ID do animal a ser removido do evento: ")
            crud.remover_animal_de_evento(idEvento, idAnimal)

        elif opcao == "0":
            break

        else:
            print("Opção inválida.")

    if __name__ == "__main__":
        menuEventosEducativos()