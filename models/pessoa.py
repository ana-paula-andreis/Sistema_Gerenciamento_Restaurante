from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome, cpf, telefone):
        self._nome = nome
        self._cpf = cpf
        self._telefone = telefone
    
    @property
    def nome(self):
        return self._nome

    @property
    def cpf(self):
        return self._cpf

    @property
    def telefone(self):
        return self._telefone

class Cliente(Pessoa):
    def __init__(self, nome, cpf, telefone, codigo_cliente):
        super().__init__(nome, cpf, telefone)
        self.codigo_cliente = codigo_cliente
        self.pontos_fidelidade = 0

    def adicionar_pontos(self, pontos):
        self.pontos_fidelidade += pontos   

class Funcionario(Pessoa):
    def __init__(self, nome, cpf, telefone, cargo, salario):
        # Passa nome, cpf e telefone para a classe pai Pessoa
        super().__init__(nome, cpf, telefone)
        self.cargo = cargo
        self.salario = salario