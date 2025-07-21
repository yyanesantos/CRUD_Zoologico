from typing import Self


class especie:
    def __init__(self, nomeCientifico, nomeComum, habitatNatural):
        self.nomeCientifico = nomeCientifico
        self.nomeComum = nomeComum
        self.habitatNatural = habitatNatural

    def setNomeCientifico(self, nomeCientifico):
        self.nomeCientifico = nomeCientifico
    
    def setNomeComum(self, nomeComum):
        self.nomeComum = nomeComum
    
    def setHabitatNatural(self, habitatNatural):
        self.habitatNatural = habitatNatural
    
    def getNomeCientifico():
        return Self.nomeCientifico
    
    def getNomeComum():
        return Self.nomeComum
    
    def getHabitatNatural():
        return Self.habitatNatural