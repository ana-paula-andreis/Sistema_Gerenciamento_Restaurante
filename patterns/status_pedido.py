from abc import ABC, abstractmethod

# Classe Abstrata base para todos os estados
class StatusPedido(ABC):
    @abstractmethod
    def proximo_estagio(self, pedido):
        pass

    @abstractmethod
    def __str__(self):
        pass

# Estado 1: Pendente
class StatusPendente(StatusPedido):
    def proximo_estagio(self, pedido):
        print(f"Pedido nº {pedido.numero_pedido} foi recebido. Mudando status para Em Preparo.")
        pedido.status = StatusEmPreparo()

    def __str__(self):
        return "Pendente"
    
# Estado 2: Em Preparo
class StatusEmPreparo(StatusPedido):
    def proximo_estagio(self, pedido):
        print(f"Pedido nº {pedido.numero_pedido} está sendo cozinhado. Mudando status para Pronto.")
        pedido.status = StatusPronto()

    def __str__(self):
        return "Em Preparo"

# Estado 3: Pronto
class StatusPronto(StatusPedido):    
    def proximo_estagio(self, pedido):
        print(f"Pedido nº {pedido.numero_pedido} está pronto para entrega. Mudando status para Entregue.")
        pedido.status = StatusEntregue()

    def __str__(self):
        return "Pronto"
    
# Estado 4: Entregue/Finalizado
class StatusEntregue(StatusPedido):
    def proximo_estagio(self, pedido):
        print(f"O pedido nº {pedido.numero_pedido} já foi entregue e finalizado. Não há próximas etapas.")

    def __str__(self):
        return "Entregue"