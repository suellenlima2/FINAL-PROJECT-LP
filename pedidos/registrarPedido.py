from vendas.vendas import carregarVendas, salvarVendas
from pagamentos.pagamentoPedido import escolherPagamento

def registrarPedido(pedido):
    vendas = carregarVendas()
    numeroPedido = len(vendas) + 1

    totalPedido = sum(item["precoTotal"] for item in pedido)

    novoPedido = {
        "id": numeroPedido,
        "pizzas": pedido,
        "totalPedidoSemDesconto": totalPedido
    }  

    metodoPagamento = escolherPagamento()
    novoPedido["pagamento"] = metodoPagamento

    vendas.append(novoPedido) 
    salvarVendas(vendas)  
    return numeroPedido