from typing import Self


class cuidadorAnimal:
    def __init__(self, idCuidadorAnimal, cpfCuidador, idAnimal):
        self.idCuidadorAnimal = idCuidadorAnimal
        self.cpfCuidador = cpfCuidador
        self.idAnimal = idAnimal

    def setIdCuidadorAnimal(self, idCuidadorAnimal):
        self.idCuidadorAnimal = idCuidadorAnimal
    
    def setCpfCuidador(self, cpfCuidador):
        self.cpfCuidador = cpfCuidador

    def setIdAnimal(self, idAnimal):
        self.idAnimal = idAnimal

    def getIdCuidadorAnimal():
        return Self.idCuidadorAnimal

    def getCpfCuidador():
        return Self.cpfCuidador
    
    def getIdAnimal():
        return Self.idAnimal