from models.cardapio import ItemCardapio
from models.mesa import Mesa
from patterns import status_pedido

class Pedido:
    def __init__(self, numero_pedido, mesa):
        self.numero_pedido = numero_pedido
        self.mesa = mesa
        self.itens = []
        self.status = status_pedido.StatusPendente()  
        self.valor_total = 0.0

    def adicionar_item(self, item):
        self.itens.append(item)
        self.valor_total += item.preco

    def avancar_status(self):
        self.status.proximo_estagio(self)