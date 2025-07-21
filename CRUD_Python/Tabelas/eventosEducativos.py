from typing import Self


class eventosEducativos:
    def __init__(self, idEvento, nome, data, duracao):
        self.idEvento = idEvento
        self.nome = nome
        self.data = data
        self.duracao = duracao

    def setIdEvento(self, idEvento):
        self.idEvento = idEvento

    def setNome(self, nome):
        self.nome = nome
    
    def setData(self, data):
        self.data = data
    
    def setDuracao(self, duracao):
        self.duracao = duracao

    def getIdEvento():
        return Self.idEvento
    
    def getNome():
        return Self.nome
    
    def getData():
        return Self.data
    
    def getDuracao():
        return Self.duracao