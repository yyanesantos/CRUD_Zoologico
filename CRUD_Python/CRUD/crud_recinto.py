from typing import Self
from Tabelas.recinto import recinto
from Database.functions import functions

class recintoCrud:
    def __init__(self, host, user, password, database):
        self.db = functions(host=host, user=user, password=password, database=database)


    def criar_recinto(self, idRecinto, local, capacidadeMaxima):
        novo = recinto(idRecinto, local, capacidadeMaxima)
        self.db.criar("recinto", novo)

    def listar_recintos(self):
        recintos = self.db.listar("recinto")
        for r in recintos:
            recinto = r
            idRecinto = recinto[0]
            local = recinto[1]
            capacidadeMaxima = recinto[2]
            print("\nRecinto")
            print(f"ID do recinto: {idRecinto}")
            print(f"Local: {local}")
            print(f"Capacidade máxima: {capacidadeMaxima}")

    def atualizar_recinto(self, idRecinto, novo_local, nova_capacidade):
        campos = ["local", "capacidadeMaxima"]
        valores = (novo_local, nova_capacidade)
        self.db.atualizar("recinto", campos, valores, "idRecinto", idRecinto)

    def remover_recinto(self, idRecinto):
        self.db.remover("recinto", "idRecinto", idRecinto)

    