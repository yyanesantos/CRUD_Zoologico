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
            on="t1.cpfCuidador = t2.cpf",
            campos="t2.nome, t2.cpf, t2.telefone",
            where="t1.idAnimal = %s",
            params=(id_animal,)
            )
            eventos = self.db.join(
            "eventosAnimais",
            "eventosEducativos",
            on="t1.idEvento = t2.idEvento",
            campos="t2.idEvento, t2.nome, t2.data, t2.duracao",
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
            if eventos:
                print("ID(s) eventos:")
                for e in eventos:
                    evento = e
                    idEvento = evento[0]
                    print(f"- {idEvento}")
            else:
                print("Sem eventos participantes.")

        

    def atualizar_animal(self, idAnimal, nome, dataNascimento, sexo, especie, recinto):
        campos = ["nome", "dataNascimento", "sexo", "especie", "recinto"]
        valores = (nome, dataNascimento, sexo, especie, recinto)
        self.db.atualizar("animal", campos, valores, "idAnimal", idAnimal)

    def remover_animal(self, idAnimal):
        cuidadores = self.db.join(
            "cuidadorAnimal",
            "cuidador",
            on="t1.cpfCuidador = t2.cpf",
            campos="t2.nome, t2.cpf, t2.telefone",
            where="t1.idAnimal = %s",
            params=(idAnimal,)
            )
        eventos = self.db.join(
            "eventosAnimais",
            "eventosEducativos",
            on="t1.idEvento = t2.idEvento",
            campos="t2.idEvento, t2.nome, t2.data, t2.duracao",
            where="t1.idAnimal = %s",
            params=(idAnimal,)
            )
        for c in cuidadores:
            cuidador = c
            cpfCuidador = cuidador[1]
            self.db.remover_dualTabela("cuidadorAnimal", {
                "cpfCuidador": cpfCuidador,
                "idAnimal": idAnimal
            }, "animal")
        for e in eventos:
            evento = e
            idEvento = evento[0]
            self.db.remover_dualTabela("eventosAnimais", {
                "idEvento": idEvento,
                "idAnimal": idAnimal
            }, "evento")
        self.db.remover("animal", "idAnimal", idAnimal)

    