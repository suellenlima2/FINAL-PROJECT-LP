#modulo I
from time import sleep

def escolherPagamento():
    print("\nEscolha o método de pagamento:")
    print("1 - Dinheiro")
    print("2 - Pix")

    opcoesPagamento = {1: "Dinheiro", 2: "Pix"}
    
    try:
        escolha = int(input("Opção: "))
        
        if (escolha == 1):
            print("\nDigite o valor necessário  para troco: ")
            troco = float(input())
            print("\nO valor do troco é de: R$ ", troco)
        elif (escolha == 2):
            print("\nPague o valor total do pedido via chave Pix: pizzariass@outlook.com")
            sleep(5)
            print("Obs.: O pedido será liberado após a confirmação do pagamento.")

        return opcoesPagamento.get(escolha, "Desconhecido")
    except ValueError:
        return "Desconhecido"