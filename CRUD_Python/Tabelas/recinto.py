from typing import Self


class recinto:
    def __init__(self, idRecinto, local, capacidadeMaxima):
        self.idRecinto = idRecinto
        self.local = local
        self.capacidadeMaxima = capacidadeMaxima
    
    def setIdRecinto(self, idRecinto):
        self.idRecinto = idRecinto
    
    def setLocal(self, local):
        self.local = local
    
    def setCapacidadeMaxima(self, capacidadeMaxima):
        self.capacidadeMaxima = capacidadeMaxima

    def getIdRecinto():
        return Self.idRecinto
    
    def getLocal():
        return Self.local
    
    def getCapacidadeMaxima():
        return Self.capacidadeMaxima