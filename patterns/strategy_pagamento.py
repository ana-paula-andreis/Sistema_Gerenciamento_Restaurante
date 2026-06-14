from abc import ABC, abstractmethod

class StrategyPagamento(ABC):
    @abstractmethod
    def calcular_total(self, valor):
        pass

class PagamentoCartao(StrategyPagamento):
    def calcular_total(self, valor):
        # Cartão adiciona uma taxa de 2%, por exemplo (ou só retorna o valor puro se preferir)
        valor_final = valor * 1.02  
        print(f"Processando pagamento no cartão (com taxa de 2%) - Valor Final: R${valor_final:.2f}")
        return valor_final

class PagamentoDinheiro(StrategyPagamento):
    def calcular_total(self, valor):
        # Dinheiro ganha 5% de desconto
        valor_final = valor * 0.95  
        print(f"Processando pagamento em dinheiro (com 5% de desconto) - Valor Final: R${valor_final:.2f}")
        return valor_final