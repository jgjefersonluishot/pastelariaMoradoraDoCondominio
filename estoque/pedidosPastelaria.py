# arquivo: pedido_pasteis_completo.py

import locale
from datetime import datetime

# Configura moeda brasileira
locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")

# Preços
PRECO_PASTEL = 3.50
BEBIDAS = {
    "Coca-Cola lata": 5.00,
    "Guaraná lata": 4.50,
    "Fanta Laranja lata": 4.50,
    "Fanta Uva lata": 4.50,
    "Suco Laranja 500ml": 6.00,
    "Suco Uva 500ml": 6.00
}

# Sabores de pastel
SABORES = [
    "Carne",
    "Frango",
    "Queijo",
    "Presunto e Queijo",
    "Mumu (Doce de leite)"
]

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
        return "Pix (chave: pasteismoradoradocondominio@gmail.com)"
    else:
        print("⚠️ Opção inválida. Usando padrão: Pix.")
        return "Pix (chave: pasteismoradoradocondominio@gmail.com)"
        

def fazer_pedido():
    print("\n========== FAÇA SEU PEDIDO ==========\n")
    atendente = input("Nome do atendente: ")
    nome = input("Nome do cliente: ")
    whatsapp = input("WhatsApp do cliente: ")
    endereco = input("Endereço do cliente: ")

    itens = []
    total = 0.0

    while True:
        print("\nEscolha o que deseja adicionar:")
        print("1 - Pastel")
        print("2 - Bebida")
        print("3 - Finalizar pedido")
        print("4 - Cancelar pedido")

        opcao = input("Opção: ")

        if opcao == "1":
            print("\nSabores de pastéis:")
            for i, sabor in enumerate(SABORES, start=1):
                print(f"{i}. {sabor}")

            escolha = int(input("Escolha o número do sabor: "))
            if 1 <= escolha <= len(SABORES):
                sabor_escolhido = SABORES[escolha - 1]
                quantidade = int(input("Quantidade: "))
                subtotal = quantidade * PRECO_PASTEL
                itens.append((f"Pastel de {sabor_escolhido}", quantidade, PRECO_PASTEL, subtotal))
                total += subtotal
                print(f"✅ {quantidade}x Pastel de {sabor_escolhido} adicionado(s).")
            else:
                print("⚠️ Opção inválida.")

        elif opcao == "2":
            print("\nBebidas disponíveis:")
            for i, (bebida, preco) in enumerate(BEBIDAS.items(), start=1):
                print(f"{i}. {bebida} - {locale.currency(preco, grouping=True)}")

            escolha = int(input("Escolha o número da bebida: "))
            if 1 <= escolha <= len(BEBIDAS):
                bebida_escolhida = list(BEBIDAS.keys())[escolha - 1]
                preco_bebida = BEBIDAS[bebida_escolhida]
                quantidade = int(input("Quantidade: "))
                subtotal = quantidade * preco_bebida
                itens.append((bebida_escolhida, quantidade, preco_bebida, subtotal))
                total += subtotal
                print(f"✅ {quantidade}x {bebida_escolhida} adicionado(s).")
            else:
                print("⚠️ Opção inválida.")

        elif opcao == "3":
            if not itens:
                print("⚠️ Nenhum item adicionado ao pedido!")
                continue

            # Data e hora
            agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            pagamento = escolher_pagamento()

            print("\n========== RESUMO DO PEDIDO ==========")
            print(f"Data e Hora: {agora}")
            print(f"Atendente: {atendente}")
            print("--------------------------------------")
            print(f"Cliente: {nome}")
            print(f"WhatsApp: {whatsapp}")
            print(f"Endereço: {endereco}")
            print("\nItens do pedido:")
            for item, qtd, preco, subtotal in itens:
                print(f"- {qtd}x {item} | {locale.currency(preco, grouping=True)} cada | Subtotal: {locale.currency(subtotal, grouping=True)}")
            print("--------------------------------------")
            print(f"Total a pagar: {locale.currency(total, grouping=True)}")
            print(f"Forma de pagamento: {pagamento}")
            print("======================================\n")
            break

        elif opcao == "4":
            print("\n❌ Pedido cancelado.\n")
            break

        else:
            print("⚠️ Opção inválida, tente novamente.")
        
  
def menu():
    while True:
        print("======================================")
        print("      BEM-VINDO AO PASTÉIS DA MORADORA")
        print("======================================")
        print("1 - Fazer pedido")
        print("2 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            fazer_pedido()
        elif opcao == "2":
            print("\nObrigado pela preferência! Volte sempre!\n")
            break
        else:
            print("\n⚠️ Opção inválida, tente novamente.\n")

if __name__ == "__main__":
    menu()      
        
        
        
        
        