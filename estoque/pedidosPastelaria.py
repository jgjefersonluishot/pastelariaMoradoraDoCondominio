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
