import json
import os
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
    print("\n1 - Cliente")
    print("2 - Funcionário")
    print("3 - Sair do sistema")
    opcao = int(input("\nDigite a opção desejada: "))
    
    if opcao == 1:
        menuCliente()
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
    menuCliente()

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
                menuCliente()
            else:
                print("\nNenhuma pizza foi pedida. Tente novamente.")
                menuCliente()

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
            menuCliente()

    except FileNotFoundError:
        print("\nArquivo de pedidos não encontrado.")
    except json.JSONDecodeError:
        print("\nErro ao ler o arquivo de pedidos.")



def menuCliente():
    print("\n------------------------------------------------")
    print("1 - Menu de pizzas")
    print("2 - Fazer pedido")
    print("3 - Consultar Pedido")
    print("4 - Cancelar Pedido")
    print("5 - Voltar ao menu inicial")
    opcao = int(input("\nDigite a opção desejada: "))
    
    if opcao == 1:
        exibirPizzas()

    elif opcao == 2:
        fazerPedido()
        
    elif opcao == 3:
        id = int(input("Digite o número do pedido: "))
        consultarPedido(id)
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
    opcao = int(input("\nDigite a opção desejada: "))
    
    if opcao == 1:
        print("Cadastrar pizza")
    elif opcao == 2:
        print("Alterar pizza")
    elif opcao == 3:
        print("Excluir pizza")
    elif opcao == 4:
        print("Consultar pedidos")
    elif opcao == 5:
        print("--------------------------")
        menuInicial()
    else:
        print("Opção inválida")
    

def main():
    print("--------------------------")
    print("Bem vindx a Pizzaria SS")
    print("--------------------------")
    menuInicial()

main()

