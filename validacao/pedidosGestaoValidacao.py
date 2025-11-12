import datetime

# Estoque inicial
estoque = {
    "pasteis": {
        "Carne": 20,
        "Frango": 20,
        "Queijo": 20,
        "Presunto e Queijo": 20,
        "Mumu (Doce de leite)": 20
    },
    "bebidas": {
        "Coca-Cola lata": 10,
        "Guaraná lata": 10,
        "Fanta Laranja lata": 10,
        "Fanta Uva lata": 10,
        "Suco Laranja 500ml": 5,
        "Suco Uva 500ml": 5
    }
}

# Preços
precos = {
    "pastel": 3.50,
    "bebidas": {
        "Coca-Cola lata": 6.00,
        "Guaraná lata": 5.00,
        "Fanta Laranja lata": 5.00,
        "Fanta Uva lata": 5.00,
        "Suco Laranja 500ml": 7.00,
        "Suco Uva 500ml": 7.00
    }
}


# Funções de validação
def validar_nome():
    while True:
        nome = input("Digite o nome do cliente: ").strip()
        if nome.replace(" ", "").isalpha():
            return nome
        print("⚠️ Digite apenas letras.")

def validar_whatsapp():
    while True:
        tel = input("Digite o WhatsApp (somente números com DDD, ex: 51999999999): ").strip()
        if tel.isdigit() and 10 <= len(tel) <= 11:
            return tel
        print("⚠️ Número inválido. Digite apenas números, com DDD.")

def validar_inteiro(mensagem):
    while True:
        qtd = input(mensagem).strip()
        if qtd.isdigit() and int(qtd) > 0:
            return int(qtd)
        print("⚠️ Digite um número válido.")

def validar_texto(mensagem):
    while True:
        texto = input(mensagem).strip()
        if texto.replace(" ", "").isalpha():
            return texto
        print("⚠️ Digite apenas letras.")

def validar_numero(mensagem):
    while True:
        numero = input(mensagem).strip()
        if numero.isdigit():
            return numero
        print("⚠️ Digite apenas números.")

def escolher_opcao(opcoes, mensagem):
    while True:
        print(mensagem)
        for i, opcao in enumerate(opcoes, 1):
            print(f"{i}. {opcao}")
        escolha = input("Escolha o número: ").strip()
        if escolha.isdigit() and 1 <= int(escolha) <= len(opcoes):
            return opcoes[int(escolha) - 1]
        print("⚠️ Escolha inválida.")

def escolher_pagamento():
    formas = ["Cartão de Crédito (Master/Visa/Elo)", "Cartão de Débito (Master/Visa/Elo)", "Pix (chave: pasteismoradoradocondominio@gmail.com)"]
    return escolher_opcao(formas, "\nFormas de pagamento:")

# Registrar pedido
def registrar_pedido():
    print("\n=== FAZER PEDIDO ===")
    cliente = validar_nome()
    whatsapp = validar_whatsapp()

    # Endereço detalhado
    logradouro = validar_texto("Digite o logradouro (ex: Rua, Av, Estrada...): ")
    endereco = validar_texto("Digite o nome da rua: ")
    numero = validar_numero("Digite o número: ")
    complemento = input("Digite o complemento (opcional): ").strip()
    bloco = input("Digite o bloco (opcional): ").strip()
    bairro = validar_texto("Digite o bairro: ")
    cidade = validar_texto("Digite a cidade: ")

    total = 0
    itens = []


