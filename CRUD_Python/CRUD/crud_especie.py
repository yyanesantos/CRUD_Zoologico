from typing import Self
from Tabelas.especie import especie
from Database.functions import functions

class especieCrud:
    def __init__(self, host, user, password, database):
        self.db = functions(host=host, user=user, password=password, database=database)

    def criar_especie(self, nomeCientifico, nomeComum, habitatNatural):
        nova = especie(nomeCientifico, nomeComum, habitatNatural)
        self.db.criar("especie", nova)

    def listar_especies(self):
        especies = self.db.listar("especie")
        for e in especies:
            especie = e
            nomeCientifico = especie[0]
            nomeComum = especie[1]
            habitatNatural = especie[2]
            print("\nEspécie")
            print(f"Nome científico: {nomeCientifico}")
            print(f"Nome comum: {nomeComum}")
            print(f"Habitat natural: {habitatNatural}")


    def atualizar_especie(self, nomeCientifico, novo_nomeComum, novo_habitat):
        campos = ["nomeComum", "habitatNatural"]
        valores = (novo_nomeComum, novo_habitat)
        self.db.atualizar("especie", campos, valores, "nomeCientifico", nomeCientifico)

    def remover_especie(self, nomeCientifico):
        self.db.remover("especie", "nomeCientifico", nomeCientifico)

    