#modulo K
import json
import os

arquivoVendas = "vendas.json"

def carregarVendas():
    if os.path.exists(arquivoVendas):
        try:
            with open(arquivoVendas, "r") as arquivo:
                return json.load(arquivo)
        except json.JSONDecodeError:
            print("Arquivo de vendas corrompido. Restaurando como vazio.")
            return []
    return []

def salvarVendas(vendas):
    with open(arquivoVendas, "w") as arquivo:
        json.dump(vendas, arquivo, indent=4)
