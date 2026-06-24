from models.cardapio import ItemCardapio
from models.mesa import Mesa
from patterns import status_pedido

class Pedido:
    def __init__(self, numero_pedido, mesa):
        self.numero_pedido = numero_pedido
        self.mesa = mesa
        self.itens = []
        #PEDIDO COMEÇA COM STATUS PENDENTE
        self.status = status_pedido.StatusPendente()  
        self.valor_total = 0.0

    def adicionar_item(self, item):
        self.itens.append(item)
        self.valor_total += item.preco
        #ACUMULANDO O VALOR TOTAL DO PEDIDO

    def avancar_status(self):
        #O PEDIDO NÃO SABE COMO MUDAR DE STATUS, ELE DELEGA ESSA RESPONSABILIDADE PARA O OBJETO STATUS
        self.status.proximo_estagio(self)