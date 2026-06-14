from models.restaurante import Restaurante
from models.mesa import Mesa
from models.cardapio import ItemCardapio
from models.pessoa import Cliente, Funcionario
from core.pedido import Pedido
from core.pagamento import Pagamento
from patterns.strategy_pagamento import PagamentoCartao, PagamentoDinheiro


if __name__ == "__main__":
    
    print("--- Inicializando o Sistema do Restaurante --- \n")

    #Criando o restaurante
    restaurante = Restaurante("Restaurante Saboroso")

    #Criando as mesas
    mesa1 = Mesa(1, 4)
    mesa2 = Mesa(2, 2)
    restaurante.lista_mesas.extend([mesa1, mesa2])

    #Registrando clientes e funcionários 
    cliente1 = Cliente("João Silva", "123.456.789-00", "54 - 123456789", "C001")
    funcionario1 = Funcionario("Maria Souza", "987.654.321-00", "54 - 987654321", "Garçom", 2000.0)
    restaurante.registrar_cliente(cliente1)
    restaurante.registrar_funcionario(funcionario1)

    #Criando itens do cardápio
    item1 = ItemCardapio("Hambúrguer", 15.0, "Prato Principal")
    item2 = ItemCardapio("Refrigerante", 5.0, "Bebida")


    #Abrindo um pedido
    pedido1 = Pedido(101, mesa1)
    pedido1.adicionar_item(item1)
    pedido1.adicionar_item(item2)
    restaurante.abrir_pedido(pedido1)

    print(f"Status inicial do pedido: {pedido1.status}")

    #SIMULANDO O PADRÃO STATE
    pedido1.avancar_status()  # Em Preparo
    pedido1.avancar_status()  # Pronto

    #Processando pagamento (STRATEGY)
    print("\n--- Processando Pagamento ---")
    pagamento = Pagamento(PagamentoCartao())
    valor_pago = pagamento.processar(pedido1.valor_total)
    
    #Pedido entregue e pago 
    pedido1.avancar_status()  # Entregue
    mesa1.ocupada = False     # Libera a mesa 

    print(f"\n--- Resumo Final ---")
    print(f"Valor original: R$ {pedido1.valor_total:.2f}")
    print(f"Valor final pago (com taxas/descontos): R$ {valor_pago:.2f}")
    print(f"Status do Pagamento: {pagamento.status_pagamento}")
    print(f"Mesa {mesa1.numero} está ocupada? {mesa1.ocupada}")