from abc import ABC, abstractmethod

#CLASSE ABSTRATA PARA ESTRATÉGIA DE PAGAMENTO
class StrategyPagamento(ABC):
    @abstractmethod
    def calcular_total(self, valor):
        pass

#ESTRATEGIA 1: CARTAO COM TAXA DE 2%
class PagamentoCartao(StrategyPagamento):
    def calcular_total(self, valor):
        #POLIMORFISMO: Cartão tem taxa de 2%
        valor_final = valor * 1.02  
        print(f"Processando pagamento no cartão (com taxa de 2%) - Valor Final: R${valor_final:.2f}")
        return valor_final

#ESTRATEGIA 2: DINHEIRO COM DESCONTO DE 5%
class PagamentoDinheiro(StrategyPagamento):
    def calcular_total(self, valor):
        #POLIMORFISMO: DINHEIRO TEM DESCONTO DE 5%
        valor_final = valor * 0.95  
        print(f"Processando pagamento em dinheiro (com 5% de desconto) - Valor Final: R${valor_final:.2f}")
        return valor_final