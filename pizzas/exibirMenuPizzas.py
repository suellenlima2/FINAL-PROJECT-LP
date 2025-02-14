from time import sleep
from pizzas.menuPizzas import MenuPizzas

def exibirPizzas():
    print("\n----------------MENU DE PIZZAS----------------")
    for pizza, dados in MenuPizzas.items():
        print(f"{pizza} - R$ {dados['preco']:.2f}")
    print("------------------------------------------------")
    sleep(4)