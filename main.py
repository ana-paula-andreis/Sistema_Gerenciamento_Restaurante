from models.restaurante import Restaurante
from models.mesa import Mesa
from models.cardapio import ItemCardapio
from models.pessoa import Cliente, Funcionario
from core.pedido import Pedido
from core.pagamento import Pagamento
from patterns.strategy_pagamento import PagamentoCartao, PagamentoDinheiro

def exibir_menu():
    print("\n" + "="*40)
    print("      SISTEMA GERENCIADOR DE RESTAURANTE      ")
    print("="*40)
    print("1. Cadastrar Mesa")
    print("2. Cadastrar Item no Cardápio")
    print("3. Abrir Novo Pedido e Lançar Itens")
    print("4. Avançar Status de um Pedido (STATE)")
    print("5. Fechar Conta e Pagar (STRATEGY)")
    print("6. Listar Visão Geral do Restaurante")
    print("0. Sair do Sistema")
    print("="*40)

if __name__ == "__main__":
    print("--- Inicializando o Sistema do Restaurante ---")
    restaurante = Restaurante("Restaurante Saboroso")

    # Massa de dados inicial automática para o sistema não iniciar totalmente vazio
    restaurante.mesas.append(Mesa(1, 4))
    restaurante.mesas.append(Mesa(2, 2))
    restaurante.cardapio.append(ItemCardapio("Hambúrguer", 15.0, "Prato Principal"))
    restaurante.cardapio.append(ItemCardapio("Refrigerante", 5.0, "Bebida"))

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("\n--- CADASTRAR MESA ---")
            numero = int(input("Número da Mesa: "))
            capacidade = int(input("Capacidade da Mesa: "))
            nova_mesa = Mesa(numero, capacidade)
            restaurante.mesas.append(nova_mesa)
            print(f"Sucesso: Mesa {numero} cadastrada!")

        elif opcao == "2":
            print("\n--- CADASTRAR ITEM CARDÁPIO ---")
            nome = input("Nome do Item: ")
            preco = float(input("Preço (ex: 15.50): "))
            categoria = input("Categoria (Prato/Bebida/Sobremesa): ")
            novo_item = ItemCardapio(nome, preco, categoria)
            restaurante.cardapio.append(novo_item)
            print(f"Sucesso: {nome} adicionado ao cardápio!")

        elif opcao == "3":
            print("\n--- ABRIR NOVO PEDIDO ---")
            if not restaurante.mesas:
                print("Erro: Não há mesas cadastradas.")
                continue
            
            print("Mesas Disponíveis:")
            for m in restaurante.mesas:
                status = "Ocupada" if m.ocupada else "Livre"
                print(f" - Mesa {m.numero} (Capacidade: {m.capacidade}) [{status}]")
            
            num_mesa = int(input("Escolha o número da mesa para o pedido: "))
            mesa_selecionada = next((m for m in restaurante.mesas if m.numero == num_mesa), None)

            if not mesa_selecionada:
                print("Erro: Mesa não encontrada.")
            elif mesa_selecionada.ocupada:
                print("Erro: Esta mesa já está ocupada por outro pedido ativo.")
            else:
                num_pedido = int(input("Defina o número/ID para este pedido: "))
                novo_pedido = Pedido(num_pedido, mesa_selecionada)
                
                print("\nCardápio Disponível:")
                for i, item in enumerate(restaurante.cardapio):
                    print(f" [{i}] {item.nome} - R$ {item.preco:.2f}")
                
                print("Insira os índices dos itens separados por espaço (ex: 0 1):")
                escolhas = input("Itens: ").split()
                
                for index in escolhas:
                    try:
                        idx = int(index)
                        novo_pedido.adicionar_item(restaurante.cardapio[idx])
                    except (ValueError, IndexError):
                        print(f"Aviso: Opção de item '{index}' inválida e ignorada.")
                
                restaurante.abrir_pedido(novo_pedido)
                print(f"\nSucesso: Pedido nº {num_pedido} aberto para a Mesa {num_mesa}!")
                print(f"Valor inicial acumulado: R$ {novo_pedido.valor_total:.2f}")

        elif opcao == "4":
            print("\n--- AVANÇAR STATUS DO PEDIDO (STATE) ---")
            if not restaurante.pedidos:
                print("Não há pedidos cadastrados.")
                continue
                
            for p in restaurante.pedidos:
                print(f" - Pedido nº {p.numero_pedido} (Mesa {p.mesa.numero}) | Status Atual: {p.status}")
                
            num_p = int(input("Digite o número do pedido que deseja avançar: "))
            pedido_selecionado = next((p for p in restaurante.pedidos if p.numero_pedido == num_p), None)
            
            if pedido_selecionado:
                print("\n[Ação do Padrão State]:")
                pedido_selecionado.avancar_status()
                print(f"Status Novo: {pedido_selecionado.status}")
            else:
                print("Erro: Pedido não encontrado.")

        elif opcao == "5":
            print("\n--- FECHAR CONTA E PAGAR (STRATEGY) ---")
            if not restaurante.pedidos:
                print("Não há pedidos abertos.")
                continue
                
            pedidos_ativos = [p for p in restaurante.pedidos if p.mesa.ocupada]
            if not pedidos_ativos:
                print("Não existem pedidos ativos aguardando fechamento.")
                continue
                
            for p in pedidos_ativos:
                print(f" - Pedido nº {p.numero_pedido} (Mesa {p.mesa.numero}) | Subtotal: R$ {p.valor_total:.2f}")
                
            num_p = int(input("Digite o número do pedido para fechar a conta: "))
            pedido_selecionado = next((p for p in pedidos_ativos if p.numero_pedido == num_p), None)
            
            if pedido_selecionado:
                print("\nFormas de Pagamento:")
                print("1. Cartão (Aplica 2% de Taxa)")
                print("2. Dinheiro/Pix (Aplica 5% de Desconto)")
                forma = input("Selecione a forma: ")
                
                if forma == "1":
                    estrategia = PagamentoCartao()
                elif forma == "2":
                    estrategia = PagamentoDinheiro()
                else:
                    print("Forma inválida. Operação cancelada.")
                    continue
                
                print("\n[Ação do Padrão Strategy]:")
                pagamento = Pagamento(estrategia)
                valor_final = pagamento.processar(pedido_selecionado.valor_total)
                
                # Sincroniza o fluxo final
                while str(pedido_selecionado.status) != "Entregue":
                    pedido_selecionado.avancar_status()
                    
                pedido_selecionado.mesa.ocupada = False
                print(f"\nConta fechada! Mesa {pedido_selecionado.mesa.numero} liberada.")
            else:
                print("Erro: Pedido ativo não encontrado.")

        elif opcao == "6":
            print("\n" + "-"*30)
            print("   VISÃO GERAL DO RESTAURANTE   ")
            print("-"*30)
            print(f"Mesas Cadastradas: {len(restaurante.mesas)}")
            for m in restaurante.mesas:
                status = "OCUPADA" if m.ocupada else "LIVRE"
                print(f" - Mesa {m.numero}: {status}")
            print(f"\nTotal de Pedidos no Histórico: {len(restaurante.pedidos)}")
            print("-"*30)

        elif opcao == "0":
            print("\nEncerrando o sistema do restaurante... Até mais!")
            break
        else:
            print("Opção inválida, tente novamente.")