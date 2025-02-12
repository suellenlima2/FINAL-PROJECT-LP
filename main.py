import json
import os
from time import sleep

MenuPizzas = {
        "Mussarela": {"preco": 25.00},
        "Calabresa": {"preco": 30.00},
        "Portuguesa": {"preco": 35.00},
        "Frango com Catupiry": {"preco": 40.00},
        "Marguerita": {"preco": 35.00},
        "Quatro Queijos": {"preco": 35.00},
        "Napolitana": {"preco": 35.00},
        "Atum": {"preco": 35.00},
        "Bacon": {"preco": 35.00},
        "Romeu e Julieta": {"preco": 35.00},
        "Chocolate": {"preco": 30.00},
        "Banana": {"preco": 30.00},
        "Brigadeiro": {"preco": 30.00}
}

def exibirPizzas():
    print("\n----------------MENU DE PIZZAS----------------")
    for pizza, dados in MenuPizzas.items():
        print(f"{pizza} - R$ {dados['preco']:.2f}")
    print("------------------------------------------------")
    sleep(2)
    menuPrincipal()

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

def registrarPedido(pedido):
    vendas = carregarVendas()
    numeroPedido = len(vendas) + 1

    totalPedido = sum(item["precoTotal"] for item in pedido)

    novoPedido = {
        "id": numeroPedido,
        "pizzas": pedido,
        "totalPedido": totalPedido
    }

    vendas.append(novoPedido) 
    salvarVendas(vendas)  
    return numeroPedido

def fazerPedido():
     pedidoCompleto = []
     continuar = 's'

     while continuar == 's':
        saborPizza = input("\nDigite o nome da pizza desejada: ").capitalize()
        
        if saborPizza in MenuPizzas:
            quantidade = int(input(f"Digite a quantidade de pizzas do sabor {saborPizza}: "))
            precoUnitario = MenuPizzas[saborPizza]["preco"]
            precoTotal = precoUnitario * quantidade
            pedidoCompleto.append({
                "pizza": saborPizza,
                "quantidade": quantidade,
                "precoUnitario": precoUnitario,
                "precoTotal": precoTotal
            })
            print(f"\nAdicionado ao pedido: {quantidade} {saborPizza}(s) - R$ {precoTotal:.2f}")
        else:
            print("\nPizza não encontrada no menu. Tente novamente.")
        
        continuar = input("\nDeseja pedir mais alguma pizza? (s/n): ").strip().lower()
        if continuar == 's':
            continue
        else:
            if pedidoCompleto:
                numeroPedido = registrarPedido(pedidoCompleto)
                totalPedido = sum(item["precoTotal"] for item in pedidoCompleto)
                print(f"\nPedido nº {numeroPedido} finalizado")
                print("Código do seu pedido: ", numeroPedido)
                
                for item in pedidoCompleto:
                    print(f"- {item['quantidade']}x {item['pizza']} (R$ {item['precoTotal']:.2f})")
                print(f"Total do pedido: R$ {totalPedido:.2f}")
                menuPrincipal()
            else:
                print("\nNenhuma pizza foi pedida. Tente novamente.")
                menuPrincipal()

def consultarPedido(id):
    try:
        with open("vendas.json", "r") as arquivo:
            pedidos = json.load(arquivo)
            
        pedidoEncontrado = next((pedido for pedido in pedidos if pedido["id"] == id), None)
        
        if pedidoEncontrado:
            print(f"\nPedido nº {pedidoEncontrado['id']}:")
            for item in pedidoEncontrado["pizzas"]:
                print(f"- {item['quantidade']}x {item['pizza']} (R$ {item['precoTotal']:.2f})")
            print(f"Total do pedido: R$ {pedidoEncontrado['totalPedido']:.2f}")
        else:
            print(f"\nPedido com ID {id} não encontrado.")
        
        opcao = input("\nDeseja consultar outro pedido? S | N: ").strip().upper()

        if opcao == 'S':
            nId = int(input("Digite o número do pedido: "))
            consultarPedido(nId)
        else:
            menuPrincipal()

    except FileNotFoundError:
        print("\nArquivo de pedidos não encontrado.")
    except json.JSONDecodeError:
        print("\nErro ao ler o arquivo de pedidos.")

def cancelarPedido():
    vendas = carregarVendas()
    
    if not vendas:
        print("\nNão há pedidos registrados.")
        return
    
    try:
        idPedido = int(input("\nDigite o ID do pedido que deseja cancelar: "))
    except ValueError:
        print("\nID inválido. Digite um número válido.")
        return cancelarPedido()

    pedidosAtualizados = [pedido for pedido in vendas if pedido["id"] != idPedido]

    if len(pedidosAtualizados) == len(vendas):
        print(f"\nPedido com ID {idPedido} não encontrado.")
    else:
        salvarVendas(pedidosAtualizados)
        print(f"\nPedido nº {idPedido} cancelado com sucesso!")

    sleep(2)
    menuPrincipal()

def menuPrincipal():
    print("\n1 - Menu de pizzas")
    print("2 - Fazer pedido")
    print("3 - Consultar Pedido")
    print("4 - Cancelar Pedido")
    print("5 - Encerrar o programa")
    opcao = int(input("\nDigite a opção desejada: "))
    
    if opcao == 1:
        exibirPizzas()

    elif opcao == 2:
        fazerPedido()
        
    elif opcao == 3:
        id = int(input("Digite o número do pedido: "))
        consultarPedido(id)
    elif opcao == 4:
        cancelarPedido()
    elif opcao == 5:
        print("Encerrando o programa...")
        sleep(2)
        exit()
    else:
        print("Opção inválida")


def main():
    print("--------------------------")
    print("Bem vindx a Pizzaria SS")
    print("--------------------------")
    menuPrincipal()

main()

