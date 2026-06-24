from abc import ABC, abstractmethod

#CLASSE ABSTRATA, SERVE DE MOLDE
class Pessoa(ABC):
    def __init__(self, nome, cpf, telefone):
        #ENCAPSULAMENTO: ATRIBUTOS PRIVADOS
        self._nome = nome
        self._cpf = cpf
        self._telefone = telefone
    
    #@PROPERTY: PERMITE ACESSAR ATRIBUTOS PRIVADOS DE FORMA SEGURA
    @property
    def nome(self):
        return self._nome

    @property
    def cpf(self):
        return self._cpf

    @property
    def telefone(self):
        return self._telefone

#HERANÇA: CLIENTE E FUNCIONARIO HERDAM DE PESSOA
class Cliente(Pessoa):
    def __init__(self, nome, cpf, telefone, codigo_cliente):
        #PASSA NOME, CPF E TELEFONE PARA A CLASSE PAI PESSOA
        super().__init__(nome, cpf, telefone)
        self.codigo_cliente = codigo_cliente #ATRIBUTO ESPECÍFICO DO CLIENTE
        self.pontos_fidelidade = 0

    def adicionar_pontos(self, pontos):
        self.pontos_fidelidade += pontos   

#HERANÇA: CLIENTE E FUNCIONARIO HERDAM DE PESSOA
class Funcionario(Pessoa):
    def __init__(self, nome, cpf, telefone, cargo, salario):
        #PASSA NOME, CPF E TELEFONE PARA A CLASSE PAI PESSOA
        super().__init__(nome, cpf, telefone)
        self.cargo = cargo #ATRIBUTO ESPECÍFICO DO FUNCIONÁRIO
        self.salario = salario #ATRIBUTO ESPECÍFICO DO FUNCIONÁRIO