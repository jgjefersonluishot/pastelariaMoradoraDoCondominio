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

print("sem bug até o momento")

