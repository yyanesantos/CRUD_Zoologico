from typing import Self


class cuidador:
    def __init__(self, nome, cpf, telefone):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone

    def setNome(self, nome):
        self.nome = nome

    def setCpf(self, cpf):
        self.cpf = cpf
    
    def setTelefone(self, telefone):
        self.telefone = telefone

    def getNome():
        return Self.nome
    
    def getCpf():
        return Self.cpf
    
    def getTelefone():
        return Self.telefone

    