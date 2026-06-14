from patterns.strategy_pagamento import StrategyPagamento

class Pagamento:
    def __init__(self, strategy):
        self.strategy = strategy
        self.valor = 0.0
        self.status_pagamento = "Pendente"

    def processar(self, valor):
        self.valor = self.strategy.calcular_total(valor)
        self.status_pagamento = "Pago"
        return self.valor