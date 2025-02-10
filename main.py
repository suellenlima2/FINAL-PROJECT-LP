import json
from time import sleep

def carregarFuncionarios():
    try:
        with open("funcionarios.json", "r", encoding="utf-8") as arquivo:
            funcionarios = json.load(arquivo)
        return funcionarios
    except FileNotFoundError:
        print("Arquivo de funcionários não encontrado.")
        return []
    except json.JSONDecodeError:
        print("Erro ao ler o arquivo JSON.")
        return []

def menuInicial():
    print("1 - Cliente")
    print("2 - Funcionário")
    print("3 - Sair do sistema")
    opcao = int(input("Digite a opção desejada: "))
    
    if opcao == 1:
        opcao = menuCliente()
    elif opcao == 2:
        funcionarios = carregarFuncionarios()

        codigoFuncionario = input("Digite o seu código de funcionário: ").strip()
        
        for funcionario in funcionarios:
            if str(funcionario["id"]) == codigoFuncionario:
                print(f"Acesso permitido! Bem-vindx, {funcionario['nome']}.")
                return menuFuncionario()

        print("Código inválido! Acesso negado.")
        return False
        
    elif opcao == 3:
        print("Até mais!")
    else:
        print("Opção inválida")

def menuPizzas():
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

    print("\n----------------MENU DE PIZZAS----------------")
    for pizza, dados in MenuPizzas.items():
        print(f"{pizza} - R$ {dados['preco']:.2f}")
    print("------------------------------------------------")
    sleep(2)
    menuCliente()


def menuCliente():
    print("1 - Menu de pizzas")
    print("2 - Fazer pedido")
    print("3 - Consultar Pedido")
    print("4 - Cancelar Pedido")
    print("5 - Voltar ao menu inicial")
    opcao = int(input("Digite a opção desejada: "))
    
    if opcao == 1:
        menuPizzas()

    elif opcao == 2:
        print("Fazer pedido")
    elif opcao == 3:
        print("Consultar Pedido")
    elif opcao == 4:
        print("Cancelar Pedido")
    elif opcao == 5:
        menuInicial()
    else:
        print("Opção inválida")

def menuFuncionario():
    print("\n---------------MENU-----------------")
    print("1 - Cadastrar pizza")
    print("2 - Alterar pizza")
    print("3 - Excluir pizza")
    print("4 - Consultar pedidos")
    print("5 - Voltar ao menu inicial")
    opcao = int(input("Digite a opção desejada: "))
    
    if opcao == 1:
        print("Cadastrar pizza")
    elif opcao == 2:
        print("Alterar pizza")
    elif opcao == 3:
        print("Excluir pizza")
    elif opcao == 4:
        print("Consultar pedidos")
    elif opcao == 5:
        menuInicial()
    else:
        print("Opção inválida")
    

def main():
    print("--------------------------")
    print("Bem vindo a Pizzaria SS")
    print("--------------------------")
    menuInicial()

main()