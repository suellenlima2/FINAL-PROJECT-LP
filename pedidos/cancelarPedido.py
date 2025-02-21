from time import sleep
from vendas.vendas import carregarVendas, salvarVendas

def cancelarPedido():
    from menuPrincipal import menuPrincipal
    vendas = carregarVendas()
    
    if not vendas:
        print("\nNão há pedidos feitos.")
        return
    
    try:
        idPedido = int(input("\nDigite o ID do pedido que deseja cancelar: "))
    except ValueError:
        print("\nID inválido. Digite um número válido.")
        return cancelarPedido()
    
    #Cria uma nova lista pedidosAtualizados, contendo todos os pedidos exceto aquele cujo ID foi inserido pelo usuário.
    pedidosAtualizados = [pedido for pedido in vendas if pedido["id"] != idPedido]

    if len(pedidosAtualizados) == len(vendas):
        print(f"\nPedido com ID {idPedido} não encontrado.")
    else:
        salvarVendas(pedidosAtualizados)
        print(f"\nPedido nº {idPedido} cancelado com sucesso!")

    sleep(2)
    menuPrincipal()