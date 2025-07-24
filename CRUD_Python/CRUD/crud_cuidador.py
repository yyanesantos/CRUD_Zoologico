from typing import Self
from Tabelas.cuidador import cuidador
from Database.functions import functions

class cuidadorCrud:
    def __init__(self, host, user, password, database):
        self.db = functions(host=host, user=user, password=password, database=database)

    def criar_cuidador(self,nome, cpf, telefone):
        novo = cuidador(nome, cpf, telefone)
        sucesso = self.db.criar("cuidador", novo)
        return sucesso

    def listar_cuidadores(self):
        cuidadores = self.db.listar("cuidador")
        for c in cuidadores:
            cuidador = c
            nome = cuidador[0]
            cpf = cuidador[1]
            telefone = cuidador[2]
            animais = self.db.join(
            "cuidadorAnimal",
            "animal",
            on="t1.idAnimal = t2.idAnimal",
            campos="t2.idAnimal",
            where="t1.cpfCuidador = %s",
            params=(cpf,)
            )
            print("\nCuidador")
            print(f"Nome: {nome}")
            print(f"CPF: {cpf}")
            print(f"Telefone: {telefone}")
            if animais:
                print("ID animais cuidados:")
                for a in animais:
                    animal = a
                    idAnimal = animal[0]
                    print(f"- {idAnimal}")
            else:
                print("Sem animais cuidados.")

    def atualizar_cuidador(self,cpf, novo_nome, novo_telefone):
        campos = ["nome", "telefone"]
        valores = (novo_nome, novo_telefone)
        self.db.atualizar("cuidador", campos, valores, "cpf", cpf)

    def remover_cuidador(self,cpf):
        animais = self.db.join(
            "cuidadorAnimal",
            "animal",
            on="t1.idAnimal = t2.idAnimal",
            campos="t2.idAnimal",
            where="t1.cpfCuidador = %s",
            params=(cpf,)
            )
        for a in animais:
            animal = a
            idAnimal = animal[0]
            self.db.remover_dualTabela("cuidadorAnimal", {
                "cpfCuidador": cpf,
                "idAnimal": idAnimal
            }, "cuidador")
        self.db.remover("cuidador", "cpf", cpf)

    def remover_animal_de_cuidador(self, cpf, idAnimal):
        self.db.remover_dualTabela("cuidadorAnimal", {
            "cpfCuidador": cpf,
            "idAnimal": idAnimal
        }, "cuidador")
    
    def adicionar_animal_ao_cuidador(self, cpf, idAnimal):
        self.db.adicionar_dualTabela("cuidadorAnimal", ["cpfCuidador", "idAnimal"], (cpf, idAnimal))