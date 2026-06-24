from models.pessoa import Cliente, Funcionario
from models.mesa import Mesa

class Restaurante:
    def __init__(self, nome):
        self.nome = nome
        #LISTAS PARA GERENCIAR MESAS, CLIENTES, FUNCIONÁRIOS, CARDÁPIO E PEDIDOS
        self.mesas = []  
        self.clientes = []
        self.funcionarios = []
        self.cardapio = []
        self.pedidos = []

    def registrar_cliente(self, cliente):
        self.clientes.append(cliente)

    def registrar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)

    def abrir_pedido(self, pedido):
        self.pedidos.append(pedido)
        pedido.mesa.ocupada = True
        #REGRA DE NEGÓCIO: AO ABRIR UM PEDIDO, A MESA FICA OCUPADA