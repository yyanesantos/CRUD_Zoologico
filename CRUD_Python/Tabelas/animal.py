from typing import Self


class animal:
    def __init__(self, idAnimal, nome, dataNascimento, sexo, especie, recinto):
        self.idAnimal = idAnimal
        self.nome = nome
        self.dataNascimento = dataNascimento
        self.sexo = sexo
        self.especie = especie
        self.recinto = recinto
    
    def setIdAnimal(self, idAnimal):
        self.idAnimal = idAnimal
    
    def setNome(self, nome):
        self.nome = nome

    def setDataNascimento(self, dataNascimento):
        self.dataNascimento = dataNascimento
    
    def setSexo(self, sexo):
        self.sexo = sexo
    
    def setEspecie(self, especie):
        self.especie = especie
    
    def setRecinto(self, recinto):
        self.recinto = recinto

    def getIdAnimal():
        return Self.idAnimal
    
    def getNome():
        return Self.nome

    def getDataNascimento():
        return Self.dataNascimento
    
    def getSexo():
        return Self.sexo
    
    def getEspecie():
        return Self.especie
    
    def getRecinto():
        return Self.recinto