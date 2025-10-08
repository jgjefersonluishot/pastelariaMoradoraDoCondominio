import locale
from datetime import datetime

from pastelariaInput.pastelariaInputOne import PRECO_PASTEL

# Configura a moeda brasileira
locale.setlocale(locale.LC_ALL,"pt_BR.UTF=8")

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