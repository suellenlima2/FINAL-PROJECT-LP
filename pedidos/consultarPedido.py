import json

def consultarPedido(id):
    from menuPrincipal import menuPrincipal
    try:
        with open("vendas.json", "r") as arquivo:
            pedidos = json.load(arquivo)
        
        #list comprehension 
        pedidoEncontrado = next((pedido for pedido in pedidos if pedido["id"] == id), None)
        
        if pedidoEncontrado:
            print(f"\nPedido nº {pedidoEncontrado['id']}:")
            for item in pedidoEncontrado["pizzas"]:
                print(f"- {item['quantidade']}x {item['pizza']} (R$ {item['precoTotal']:.2f})")
            print(f"Total do pedido(sem desconto): R$ {pedidoEncontrado['totalPedidoSemDesconto']:.2f}")
        else:
            print(f"\nPedido com ID {id} não encontrado.")
        
        opcao = input("\nDeseja consultar outro pedido? S | N: ").strip().upper()
 
        if opcao == 'S':
            nId = int(input("Digite o número do pedido que você deseja consultar: "))
            consultarPedido(nId)
        else:
            menuPrincipal()

    except FileNotFoundError:
        print("\nArquivo de pedidos não encontrado.")
    except json.JSONDecodeError:
        print("\nErro ao ler o arquivo de pedidos.")