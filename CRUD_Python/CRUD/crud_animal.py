from typing import Self
from Tabelas.animal import animal
from Database.functions import functions

class animalCrud:
    def __init__(self, host, user, password, database):
        self.db = functions(host=host, user=user, password=password, database=database)

    def criar_animal(self,idAnimal, nome, dataNascimento, sexo, especie, recinto):
        novo = animal(idAnimal, nome, dataNascimento, sexo, especie, recinto)
        self.db.criar("animal", novo)

    def listar_animais(self):
        animais = self.db.listar("animal")
        for a in animais:
            animal = a
            id_animal = animal[0]
            nome = animal[1].capitalize()
            data_nasc = animal[2].strftime("%d/%m/%Y")  # formata a data para dia/mês/ano
            sexo = animal[3]
            especie = animal[4]
            id_recinto = animal[5]
            cuidadores = self.db.join(
            "cuidadorAnimal",
            "cuidador",
            on="t1.cpfCuidador = t2.cpfCuidador",
            campos="t2.cpfCuidador",
            where="t1.idAnimal = %s",
            params=(id_animal,)
            )

            print("\nAnimal")
            print(f"ID: {id_animal}")
            print(f"Nome: {nome}")
            print(f"Data de nascimento: {data_nasc}")
            print(f"Sexo: {sexo}")
            print(f"Espécie: {especie}")
            print(f"ID do recinto: {id_recinto}")
            if cuidadores:
                print("CPF Cuidadores:")
                for c in cuidadores:
                    cuidador = c
                    cpfCuidador = cuidador[1]
                    print(f"- {cpfCuidador}")
            else:
                print("Sem cuidadores.")

        

    def atualizar_animal(self, idAnimal, nome, dataNascimento, sexo, especie, recinto):
        campos = ["nome", "dataNascimento", "sexo", "especie", "recinto"]
        valores = (nome, dataNascimento, sexo, especie, recinto)
        self.db.atualizar("animal", campos, valores, "idAnimal", idAnimal)

    def remover_animal(self, idAnimal):
        self.db.remover("animal", "idAnimal", idAnimal)

    