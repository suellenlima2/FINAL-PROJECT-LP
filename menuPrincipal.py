import sys
from pizzas.exibirMenuPizzas import exibirPizzas
from pedidos.fazerPedido import fazerPedido
from pedidos.consultarPedido import consultarPedido
from pedidos.cancelarPedido import cancelarPedido
from time import sleep

def menuPrincipal():
    while True:
        print("\n1 - Menu de pizzas")
        print("2 - Fazer pedido")
        print("3 - Consultar Pedido")
        print("4 - Cancelar Pedido")
        print("5 - Encerrar o programa")
        
        try:
            opcao = int(input("\nDigite a opção desejada: "))
            if opcao == 1:
                sleep(1)
                exibirPizzas()
                continue
            elif opcao == 2:
                sleep(1)
                fazerPedido()
            elif opcao == 3:
                sleep(1)
                idPedido = int(input("Digite o número do pedido que você deseja consultar: "))
                consultarPedido(idPedido)
            elif opcao == 4:
                sleep(1)
                cancelarPedido()
            elif opcao == 5:
                sleep(1)
                print("Volte Sempre!!!")
                sleep(3)  
                sys.exit()
            else:
                print("Opção inválida")
        except ValueError:
            print("Entrada inválida. Tente novamente.")
