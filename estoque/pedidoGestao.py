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






