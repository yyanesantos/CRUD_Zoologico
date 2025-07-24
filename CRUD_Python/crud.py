from Menu.menu_animal import menuAnimal
from Menu.menu_cuidador import menuCuidador
from Menu.menu_especie import menuEspecie
from Menu.menu_eventosEducativos import menuEventosEducativos
from Menu.menu_recinto import menuRecinto

def menuPrincipal():
    while True:
        print("\n🐾 Zoológico")
        print("")
        print("1. Animal")
        print("2. Cuidador")
        print("3. Espécie")
        print("4. Eventos Educativos")
        print("5. Recinto")
        print("0. Sair")

        opcao = input("Escolha a opção que você deseja visualizar: ")
        if opcao == "1":
            menuAnimal()
        if opcao == "2":
            menuCuidador()
        if opcao == "3":
            menuEspecie()
        if opcao == "4":
            menuEventosEducativos()
        if opcao == "5":
            menuRecinto()
        elif opcao == "0":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida.")

menuPrincipal()