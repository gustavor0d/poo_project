import os
from datetime import datetime

def cls():
    return os.system("cls")

def valor_entrada(table, prompt):
    valor = input(prompt)
    if valor == '0':
        cls()
        print(f"\nCadastro de {table} cancelado.")
        return None
    return valor

data = datetime.today().date()

def data_format(data_pedido):
    if not data_pedido:
        return "Não localizada"
    return data_pedido.strftime("%d/%m/%Y")
