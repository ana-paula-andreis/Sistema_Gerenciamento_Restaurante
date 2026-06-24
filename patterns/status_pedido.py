from abc import ABC, abstractmethod

#CLASSE ABSTRATA PARA OS ESTADOS DO PEDIDO
class StatusPedido(ABC):
    @abstractmethod
    def proximo_estagio(self, pedido):
        pass

    @abstractmethod
    def __str__(self):
        pass

#ESTADO INICIAL: PENDENTE
class StatusPendente(StatusPedido):
    def proximo_estagio(self, pedido):
        print(f"Pedido nº {pedido.numero_pedido} foi recebido. Mudando status para Em Preparo.")
        pedido.status = StatusEmPreparo()

    def __str__(self):
        return "Pendente"
    
#ESTADO 2: EM PREPARO
class StatusEmPreparo(StatusPedido):
    def proximo_estagio(self, pedido):
        print(f"Pedido nº {pedido.numero_pedido} está sendo cozinhado. Mudando status para Pronto.")
        #POLIMORFISMO: MUDANDO O ESTADO DO PEDIDO PARA PRONTO
        pedido.status = StatusPronto()

    def __str__(self):
        return "Em Preparo" 

#ESTADO 3: PRONTO
class StatusPronto(StatusPedido):    
    def proximo_estagio(self, pedido):
        print(f"Pedido nº {pedido.numero_pedido} está pronto para entrega. Mudando status para Entregue.")
        pedido.status = StatusEntregue()

    def __str__(self):
        return "Pronto"
    
#ESTADO FINAL: ENTREGUE
class StatusEntregue(StatusPedido):
    def proximo_estagio(self, pedido):
        print(f"O pedido nº {pedido.numero_pedido} já foi entregue e finalizado. Não há próximas etapas.")

    def __str__(self):
        return "Entregue"