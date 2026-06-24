# Sistema de Gerenciamento de Restaurante

## 🎯 Objetivo do Projeto
Este sistema foi desenvolvido como parte da Avaliação Prática da disciplina de Tecnologia Orientada a Objetos (TOO). O objetivo é gerenciar o fluxo operacional de um restaurante, desde o controle de mesas e funcionários até a abertura, acompanhamento de produção e pagamento de pedidos.

## 📐 Diagrama de Classes
<img width="1384" height="428" alt="image" src="https://github.com/user-attachments/assets/05764db2-cd75-4ce2-9c7f-83dfc7c5218e" />

## 🧬 Aplicação dos Pilares da POO
* **Abstração:** Representação simplificada de entidades em classes como `Mesa`, `ItemCardapio` e `Pedido`.
* **Encapsulamento:** Os atributos críticos da classe `Pessoa` (como `_nome`, `_cpf`) utilizam modificadores de acesso protegidos e métodos `property` (getters) para garantir a integridade dos dados.
* **Herança:** A classe abstrata `Pessoa` serve como classe base para `Cliente` e `Funcionario`, reaproveitando atributos comuns.
* **Polimorfismo:** Aplicado fortemente na execução das classes de comportamento do Padrão State e Strategy, onde objetos de diferentes subclasses respondem ao mesmo método de assinaturas idênticas de formas distintas.

## 🛠️ Padrões de Projeto Utilizados
### 1. State Pattern
Utilizado para controlar o ciclo de vida dinâmico da classe `Pedido`. O pedido transiciona entre os estados `StatusPendente ➡️ StatusEmPreparo ➡️ StatusPronto ➡️ StatusEntregue`, delegando o comportamento de transição para classes especialistas de estado (`StatusPedido`).

### 2. Strategy Pattern 
Adotado na classe `Pagamento` para isolar os algoritmos de cálculo de preço (taxas ou descontos) baseados na escolha do cliente. O sistema pode alternar em tempo de execução entre `PagamentoPix` (que concede 5% de desconto) e `PagamentoCartao` (que aplica taxa de 2%), sem alterar a estrutura da classe de negócio.

## 🤖 Declaração de Uso de IA
* Utilizei IA como ferramenta de apoio.
* **Ferramenta(s):** Gemini
* **Finalidade:** Estruturação inicial do esqueleto de herança em Python e apoio na documentação técnica dos padrões aplicados.
  
