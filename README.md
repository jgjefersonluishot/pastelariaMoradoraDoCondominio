# Pastelaria Moradora do Condominio
Linguagem Python desenvolvimento em console.
# Print
Os arquivos `pastelaria_one.py` e `pastelaria_two.py` são **programas simples em Python** que usam apenas o comando `print()`.
## O que eles fazem?
- Quando executados, mostram no **terminal** um anúncio de venda de pastéis.
- Todo o conteúdo (título, sabores, preço, contatos) aparece formatado com `print()`.
## Diferença entre eles
- **`pastelaria_one.py`**
  - Texto mais pessoal ("sou moradora do condomínio").
  - Lista 4 sabores.
  - Mostra 2 números de contato.
  - Cita um grupo de WhatsApp.

- **`pastelaria_two.py`**
  - Texto mais direto e objetivo.
  - Lista 5 sabores (inclui presunto e queijo).
  - Mostra apenas 1 número de WhatsApp.
  - Dá mais destaque ao preço.
## Resumindo
Esses programas são exemplos de como o Python pode ser usado para **imprimir mensagens formatadas** na tela.  
Eles não têm cálculos nem entradas do usuário — apenas exibem um texto pronto.
# Input🥟 Sistema de Pedidos — Pastéis da Moradora
Os arquivos `pastelaria_input_one.py` e `pastelaria_input_two.py` são **programas com entrada de dados em Python** que usam o comando `print()` e `input()` .

O arquivo **`pastelariaInputOne.py`** é um programa simples em **Python** que simula um **sistema de pedidos de pastéis** feito diretamente pelo terminal.

---

## 🧾 Função geral
O script permite que o usuário:
1. Escolha um sabor de pastel entre opções pré-definidas;  
2. Informe seus dados (nome, WhatsApp e endereço);  
3. Indique a quantidade desejada;  
4. Receba um **resumo do pedido**, com o **valor total formatado em reais (R$)**.

---

## ⚙️ Principais partes do código

### 1. Configuração de moeda
```python
locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")

PRECO_PASTEL = 3.50
sabores = ["Carne", "Frango", "Queijo", "Presunto e Queijo", "Mumu (Doce de leite)"]

========== RESUMO DO PEDIDO ==========
Cliente: Ana Souza
WhatsApp: (51) 99999-9999
Endereço: Rua das Flores, 123
Sabor escolhido: Queijo
Quantidade: 3
Valor total: R$ 10,50
======================================
💡 Em resumo

pedido_pasteis.py é um programa interativo de linha de comando que:

Simula pedidos de pastéis;

Calcula automaticamente o valor total;

Exibe um resumo bonito e formatado em reais;

Funciona em loop até o usuário escolher sair.




