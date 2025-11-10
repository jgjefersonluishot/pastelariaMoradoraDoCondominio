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
        
        
        
        
        
        
        
        