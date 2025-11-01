# arquivo: pastelaria_unificado.py

import locale
from datetime import datetime

# Configura moeda brasileira
locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")

# Estoque inicial (pode ser ajustado conforme a produção do dia)
ESTOQUE = {
    "Pastel de Carne": {"preco": 3.50, "quantidade": 20},
    "Pastel de Frango": {"preco": 3.50, "quantidade": 20},
    "Pastel de Queijo": {"preco": 3.50, "quantidade": 20},
    "Pastel de Presunto e Queijo": {"preco": 3.50, "quantidade": 20},
    "Pastel de Mumu (Doce de leite)": {"preco": 3.50, "quantidade": 20},
    "Coca-Cola lata": {"preco": 5.00, "quantidade": 15},
    "Guaraná lata": {"preco": 4.50, "quantidade": 15},
    "Fanta Laranja lata": {"preco": 4.50, "quantidade": 15},
    "Fanta Uva lata": {"preco": 4.50, "quantidade": 15},
    "Suco Laranja 500ml": {"preco": 6.00, "quantidade": 10},
    "Suco Uva 500ml": {"preco": 6.00, "quantidade": 10}
}

# Registro do movimento diário
MOVIMENTO = []

# ----- FUNÇÕES DO SISTEMA -----

def escolher_pagamento():
    print("\nFormas de pagamento disponíveis:")
    print("1 - Cartão Crédito (Visa/Master/Elo)")
    print("2 - Cartão Débito (Visa/Master/Elo)")
    print("3 - Pix (chave: pasteismoradoradocondominio@gmail.com)")

    opcao = input("Escolha a forma de pagamento: ")
    if opcao == "1":
        return "Cartão de Crédito"
    elif opcao == "2":
        return "Cartão de Débito"
    elif opcao == "3":
        return "Pix (pasteismoradoradocondominio@gmail.com)"
    else:
        print("⚠️ Opção inválida. Usando Pix.")
        return "Pix (pasteismoradoradocondominio@gmail.com)"

def mostrar_estoque():
    print("\n========== ESTOQUE DISPONÍVEL ==========")
    for produto, dados in ESTOQUE.items():
        print(f"{produto}: {dados['quantidade']} un. | {locale.currency(dados['preco'], grouping=True)} cada")
    print("========================================\n")



print("sem bug até o momento")

def fazer_pedido():
    print("\n========== FAÇA SEU PEDIDO ==========\n")
    atendente = input("Nome do atendente: ")
    nome = input("Nome do cliente: ")
    whatsapp = input("WhatsApp do cliente: ")
    endereco = input("Endereço do cliente: ")

    itens = []
    total = 0.0

    while True:
        mostrar_estoque()
        print("1 - Adicionar produto")
        print("2 - Finalizar pedido")
        print("3 - Cancelar pedido")
        opcao = input("Opção: ")

        if opcao == "1":
            produtos = list(ESTOQUE.keys())
            for i, produto in enumerate(produtos, start=1):
                preco = ESTOQUE[produto]["preco"]
                qtd = ESTOQUE[produto]["quantidade"]
                print(f"{i}. {produto} - {locale.currency(preco, grouping=True)} (Estoque: {qtd})")

            escolha = int(input("Escolha o número do produto: "))
            if 1 <= escolha <= len(produtos):
                produto_escolhido = produtos[escolha - 1]
                quantidade = int(input("Quantidade: "))

                if quantidade <= ESTOQUE[produto_escolhido]["quantidade"]:
                    preco_unit = ESTOQUE[produto_escolhido]["preco"]
                    subtotal = quantidade * preco_unit
                    itens.append((produto_escolhido, quantidade, preco_unit, subtotal))
                    total += subtotal
                    ESTOQUE[produto_escolhido]["quantidade"] -= quantidade
                    print(f"✅ {quantidade}x {produto_escolhido} adicionado(s).")
                else:
                    print("⚠️ Estoque insuficiente!")
            else:
                print("⚠️ Opção inválida.")

        elif opcao == "2":
            if not itens:
                print("⚠️ Nenhum item adicionado.")
                continue

            agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            pagamento = escolher_pagamento()

            # Resumo do pedido
            print("\n========== RESUMO DO PEDIDO ==========")
            print(f"Data e Hora: {agora}")
            print(f"Atendente: {atendente}")
            print("--------------------------------------")
            print(f"Cliente: {nome}")
            print(f"WhatsApp: {whatsapp}")
            print(f"Endereço: {endereco}")
            print("\nItens do pedido:")
            for item, qtd, preco, subtotal in itens:
                print(f"- {qtd}x {item} | {locale.currency(preco, grouping=True)} cada | {locale.currency(subtotal, grouping=True)}")
            print("--------------------------------------")
            print(f"Total a pagar: {locale.currency(total, grouping=True)}")
            print(f"Forma de pagamento: {pagamento}")
            print("======================================\n")

            # Registro no movimento diário
            MOVIMENTO.append({"data": agora, "cliente": nome, "total": total, "pagamento": pagamento})

            break

        elif opcao == "3":
            print("\n❌ Pedido cancelado.\n")
            break
        else:
            print("⚠️ Opção inválida.")


def mostrar_movimento():
    print("\n========== MOVIMENTO DIÁRIO ==========")
    total_vendas = 0
    for pedido in MOVIMENTO:
        print(f"{pedido['data']} | Cliente: {pedido['cliente']} | Valor: {locale.currency(pedido['total'], grouping=True)} | Pagamento: {pedido['pagamento']}")
        total_vendas += pedido['total']
    print("--------------------------------------")
    print(f"Total vendido no dia: {locale.currency(total_vendas, grouping=True)}")
    print("======================================\n")


def menu():
    while True:
        print("======================================")
        print("      PASTELARIA DA MORADORA")
        print("======================================")
        print("1 - Fazer pedido")
        print("2 - Ver movimento do dia")
        print("3 - Ver estoque atual")
        print("4 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            fazer_pedido()
        elif opcao == "2":
            mostrar_movimento()
        elif opcao == "3":
            mostrar_estoque()
        elif opcao == "4":
            print("\n✅ Sistema encerrado. Obrigado!\n")
            break
        else:
            print("\n⚠️ Opção inválida!\n")


if __name__ == "__main__":
    menu()





