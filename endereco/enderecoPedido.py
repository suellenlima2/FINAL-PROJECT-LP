#modulo F
import random

def enderecoEntrega():
    tempo = random.randint(30, 90)
    resp = input("\nPedido para entrega ou retirada?").strip().lower()
    if resp == 'entrega':
        print("\nPor favor, insira o endereço de entrega[cidade, bairro, numero]: ")
        endereco = input()
        print(f"\nPedido será entregue em: {endereco} em até {tempo} minutos.")
    elif resp == 'retirada':
        print("\nVá a nossa loja no endereço: Rua dos Bobos, nº 0")
        print(f"Seu pedido estará pronto em {tempo} minutos.")
    else:
        print("Opção inválida. Tente novamente.")
        enderecoEntrega()