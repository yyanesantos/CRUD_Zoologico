from CRUD.crud_especie import especieCrud

def menuEspecie():
    crud = especieCrud(host="localhost", user="root", password="12345678", database="zoologicoo")
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
            crud.criar_especie(nomeCientifico, nomeComum, habitatNatural)

        elif opcao == "2":
            crud.listar_especies()

        elif opcao == "3":
            nomeCientifico = input("Nome científico da espécie a atualizar: ")
            novo_nomeComum = input("Novo nome comum: ")
            novo_habitat = input("Novo habitat natural: ")
            crud.atualizar_especie(nomeCientifico, novo_nomeComum, novo_habitat)

        elif opcao == "4":
            nomeCientifico = input("Nome científico da espécie a remover: ")
            crud.remover_especie(nomeCientifico)

        elif opcao == "0":
            break

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menuEspecie()