import locale


# Config e formatação moeda Brasil.
locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")

# Preço do pastel
PRECO_PASTEL = 3.50

# Lista de sabores disponiveis
sabores = ["Carne", "Frango", "Queijo", "Presundo e Queijo", "Mumu (Doce de Leite)"]

# Fazer pedido
def fazer_pedido():
    print("\n=============== FAÇA O SEU PEDIDO ===================")
    nome = input("Digite o seu nome: ")
    whatsapp = input("Digite o seu WhatsApp: ")
    endereco = input("Digite o seu endereço: ")

    print("\nSabores disponíveis: ")
    for i, sabor in enumerate(sabores, start=1):
        print(f"{1}. {sabor}")

    escolha = int(input("\nEscolha o número do sabor: "))
    if 1<= escolha <= len(sabores):
        sabor_escolhido = sabores[escolha - 1]
    else:
        print("Opção inválida! Pedido Cancelado.")

    quantidade = int(input("Quantos pastéis deseja? "))

    valor_total = quantidade * PRECO_PASTEL
    valor_formatado = locale.currency(valor_total,grouping=True)

    print("\n=============== RESUMO DO PEDIDO ===================")
    print(f"Cliente: {nome}")
    print(f"WhatsApp: {whatsapp}")
    print(f"Endereço: {endereco}")
    print(f"Sabor escolhido: {sabor_escolhido}")
    print(f"Quantidade: {quantidade}")
    print(f"Valor total: {valor_formatado}")
    print("\n=====================================================")






