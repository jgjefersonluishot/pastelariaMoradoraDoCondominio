import locale
from datetime import datetime

from pastelariaInput.pastelariaInputOne import PRECO_PASTEL

# Configura a moeda brasileira
locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")

# Preço do pastel
PRECO_PASTEL=3.50

# Lista de sabores disponiveis
sabores = ["Carne", "Frango", "Queijo", "Presunto e Queijo", "Mumu (Doce de leite)"]

# funções


def fazer_pedito():
    print("\n=============== FAÇA O SEU PEDIDO =================")
    atendente = input("Nome do atendente: ")
    nome = input("Nome do cliente: ")
    whatsapp = input("WhatsApp do cliente: ")
    endereco = input("Endereço do cliente: ")

    print("\nSabores disponiveis: ")
    for i, sabor in enumerate(sabores, start=1):
        print(f"{i}. {sabor}")

    escolha = int(input("\nEscolha o número do sabor: "))
    if 1 <= escolha <=len(sabores):
        sabor_escolhido = sabores[escolha-1]
    else:
        print("⚠️ Opção inválida! Pedido cancelado.")
        return

    quantidade =int(input("Quantidade de pastéis: "))

    # Calcula valor total
    valor_total = quantidade * PRECO_PASTEL
    valor_formatado = locale.currency(valor_total, grouping=True)

    # Data e hora do pedido
    agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    print("\n=============== RESUMO DO PEDIDO =================")
    print(f"Data e Hora: {agora}")
    print(f"Atendente: {atendente}")
    print("-----------------------------------------------------")
    print(f"Cliente: {nome}")
    print(f"WhatsApp: {whatsapp}")
    print(f"Endereço: {endereco}")
    print(f"Sabor escolhido: {sabor_escolhido}")
    print(f"Quantidade: {quantidade}")
    print(f"Valor total: {valor_formatado}")
    print("=====================================================")

def menu():
    while True:
        print("=====================================================")
        print("    Bem vindo Pastelaira da Moradora do Condominio   ")
        print("=====================================================")
        print("1 - Fazer pedido")
        print("2 - Sair")








