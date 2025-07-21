from typing import Self


class eventosAnimais:
    def __init__(self, idEventosAnimais, idEvento, idAnimal):
        self.idEventosAnimais = idEventosAnimais
        self.idEvento = idEvento
        self.idAnimal = idAnimal

    def setIdEventosAnimais(self, idEventosAnimais):
        self.idEventosAnimais = idEventosAnimais
    
    def setIdEvento(self, idEvento):
        self.idEvento = idEvento
    
    def setIdAnimal(self, idAnimal):
        self.idAnimal = idAnimal
    
    def getIdEventosAnimais():
        return Self.idEventosAnimais

    def getIdEvento():
        return Self.idEvento
    
    def getIdAnimal():
        return Self.idAnimal