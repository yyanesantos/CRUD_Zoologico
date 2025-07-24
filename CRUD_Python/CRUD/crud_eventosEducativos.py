from typing import Self
from Tabelas.eventosEducativos import eventosEducativos
from Database.functions import functions

class eventosEducativosCrud:
    def __init__(self, host, user, password, database):
        self.db = functions(host=host, user=user, password=password, database=database)

    def criar_evento(self, idEvento, nome, data, duracao):
        novo = eventosEducativos(idEvento, nome, data, duracao)
        sucesso = self.db.criar("eventosEducativos", novo)
        return sucesso

    def listar_eventos(self):
        eventos = self.db.listar("eventosEducativos")
        for e in eventos:
            evento = e
            idEvento = evento[0]
            nome = evento[1]
            data = evento[2]
            duracao = evento[3]
            animais = self.db.join(
            "eventosAnimais",
            "animal",
            on="t1.idAnimal = t2.idAnimal",
            campos="t2.idAnimal",
            where="t1.idEvento = %s",
            params=(idEvento,)
            )
            print("\nEvento")
            print(f"ID do evento: {idEvento}")
            print(f"Nome: {nome}")
            print(f"Data do evento: {data}")
            print(f"Duração do evento: {duracao}h")
            if animais:
                print("ID animais no evento:")
                for a in animais:
                    animal = a
                    idAnimal = animal[0]
                    print(f"- {idAnimal}")
            else:
                print("Sem animais no evento.")

    def atualizar_evento(self, idEvento, nome, data, duracao):
        campos = ["nome", "data", "duracao"]
        valores = (nome, data, duracao)
        self.db.atualizar("eventosEducativos", campos, valores, "idEvento", idEvento)

    def remover_evento(self, idEvento):
        animais = self.db.join(
            "eventosAnimais",
            "animal",
            on="t1.idAnimal = t2.idAnimal",
            campos="t2.idAnimal",
            where="t1.idEvento = %s",
            params=(idEvento,)
            )
        for a in animais:
            animal = a
            idAnimal = animal[0]
            self.db.remover_dualTabela("eventosAnimais", {
            "idEvento": idEvento,
            "idAnimal": idAnimal
        }, "evento")
        self.db.remover("eventosEducativos", "idEvento", idEvento)

    def remover_animal_de_evento(self, idEvento, idAnimal):
        self.db.remover_dualTabela("eventosAnimais", {
            "idEvento": idEvento,
            "idAnimal": idAnimal
        }, "evento")

    def adicionar_animal_de_evento(self, idEvento, idAnimal):
        self.db.adicionar_dualTabela("eventosAnimais", ["idEvento", "idAnimal"], (idEvento, idAnimal))