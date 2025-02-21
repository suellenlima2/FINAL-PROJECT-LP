from time import sleep
from pizzas.exibirMenuPizzas import MenuPizzas
from pedidos.registrarPedido import registrarPedido
from desconto.descontoPedido import aplicarDesconto
from endereco.enderecoPedido import enderecoEntrega

def formatarNomePizza(nome):
    palavras = nome.split()
    if len(palavras) >= 3:
        palavras[0] = palavras[0].capitalize()
        palavras[1] = palavras[1].capitalize()
        palavras[2] = palavras[2].capitalize()
    elif len(palavras) == 2:
        palavras[0] = palavras[0].capitalize()
        palavras[1] = palavras[1].capitalize()
    elif len(palavras) == 1:
        palavras[0] = palavras[0].capitalize()
    return " ".join(palavras)

def fazerPedido():
     from menuPrincipal import menuPrincipal
     pedidoCompleto = []
     continuar = 's'

     while continuar == 's':
        sleep(1)
        saborPizza = input("\nDigite o nome da pizza desejada: ")
        saborPizza = formatarNomePizza(saborPizza)  

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
                totalPedido = sum(item["precoTotal"] for item in pedidoCompleto)
                print("\nValor total do pedido: ", totalPedido)
                print("\nATENCAO: Utilize o cupom PIZZA10 para ganhar 10% de desconto em sua compra acima de 100.00!")
                print("ATENCAO: Utilize o cupom DOCEPIZZA para ganhar 15% de desconto em  pedidos só de pizzas doces!")
                totalPedido = aplicarDesconto(totalPedido, pedidoCompleto)
                numeroPedido = registrarPedido(pedidoCompleto)
                print(f"\nPedido nº {numeroPedido} finalizado")
                print("Código do seu pedido: ", numeroPedido)
                
                for item in pedidoCompleto:
                    print(f"- {item['quantidade']}x {item['pizza']} (R$ {item['precoTotal']:.2f})")
                print(f"Total do pedido: R$ {totalPedido:.2f}")
                enderecoEntrega()
                menuPrincipal()
            else:
                print("\nNenhuma pizza foi pedida. Tente novamente.")
                menuPrincipal()

