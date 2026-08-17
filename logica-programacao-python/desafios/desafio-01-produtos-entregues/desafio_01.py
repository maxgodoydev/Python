# Desafio 1 - Calcular vendas entregues
# 23/06/2026

produtos = [

    {"nome": "Teclado", "valor": 250, "entregue": True},
    {"nome": "Mouse", "valor": 120, "entregue": False},
    {"nome": "Monitor", "valor": 900, "entregue": True},
    {"nome": "Headset", "valor": 180, "entregue": True},
]

total_vendas_entregues = 0

for produto in produtos:
    if produto["entregue"]:
        total_vendas_entregues += produto["valor"]


print("O valor total dos produtos entregues é: ", total_vendas_entregues)
