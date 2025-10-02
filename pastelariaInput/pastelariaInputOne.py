# arquivo: pedido_pasteis.py

import locale

# Configura a formatação para moeda brasileira
locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")

# Preço do pastel
PRECO_PASTEL = 3.50

# Lista de sabores disponíveis
sabores = ["Carne", "Frango", "Queijo", "Presunto e Queijo", "Mumu (Doce de leite)"]

def fazer_pedido():
    print("\n========== FAÇA SEU PEDIDO ==========\n")
    nome = input("Digite seu nome: ")
    whatsapp = input("Digite seu WhatsApp: ")
    endereco = input("Digite seu endereço: ")

    print("\nSabores disponíveis:")
    for i, sabor in enumerate(sabores, start=1):
        print(f"{i}. {sabor}")

    escolha = int(input("\nEscolha o número do sabor: "))
    if 1 <= escolha <= len(sabores):
        sabor_escolhido = sabores[escolha - 1]
    else:
        print("Opção inválida! Pedido cancelado.")
        return

    quantidade = int(input("Quantos pastéis deseja? "))

    valor_total = quantidade * PRECO_PASTEL
    valor_formatado = locale.currency(valor_total, grouping=True)

    print("\n========== RESUMO DO PEDIDO ==========")
    print(f"Cliente: {nome}")
    print(f"WhatsApp: {whatsapp}")
    print(f"Endereço: {endereco}")
    print(f"Sabor escolhido: {sabor_escolhido}")
    print(f"Quantidade: {quantidade}")
    print(f"Valor total: {valor_formatado}")
    print("======================================\n")

def menu():
    while True:
        print("======================================")
        print("   BEM-VINDO AO PASTÉIS DA MORADORA   ")
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
            print("\nOpção inválida, tente novamente.\n")

if __name__ == "__main__":
    menu()
