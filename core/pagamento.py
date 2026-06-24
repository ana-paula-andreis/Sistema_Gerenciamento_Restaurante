from patterns.strategy_pagamento import StrategyPagamento

class Pagamento:
    def __init__(self, strategy):
        self.strategy = strategy
        self.valor = 0.0
        #RECEBE O STATUS DO PAGAMENTO, INICIALMENTE PENDENTE
        self.status_pagamento = "Pendente"

    def processar(self, valor):
        #DELEGA O CÁLCULO DO VALOR FINAL PARA A ESTRATÉGIA ESCOLHIDA
        self.valor = self.strategy.calcular_total(valor)
        self.status_pagamento = "Pago"
        return self.valor