#módulo E
cupom = {
    "PIZZA10": 0.10,  # 10% de desconto para compras acima de 100.00
    "DOCEPIZZA": 0.15,  # 15% de desconto para pedidos só de pizzas doces
    "PEDEMAIS5": 0.05  # 5% de desconto para qualquer pedido
}

def aplicarDesconto(total, pedido):
    while True:
        print("\nVocê tem um cupom de desconto? Digite o código ou pressione ENTER para continuar: ")
        cupomDigitado = input().strip().upper()
        
        if cupomDigitado in cupom:
            if cupomDigitado == "PIZZA10" and total >= 100.00:
                desconto = total * cupom[cupomDigitado]
            elif cupomDigitado == "DOCEPIZZA" and all(p["pizza"] in ["Chocolate", "Banana", "Brigadeiro", "Romeu e Julieta"] for p in pedido):
                desconto = total * cupom[cupomDigitado]
            elif cupomDigitado == "PEDEMAIS5":
                desconto = total * cupom[cupomDigitado]
            else:
                print("\nCupom não aplicável para este pedido. Tente Novamente.")
                continue
        
            totalComDesconto = total - desconto
            print(f"\nDesconto aplicado: R$ {desconto:.2f}")
            print(f"Total com desconto: R$ {totalComDesconto:.2f}")
            return totalComDesconto
    
        print("\nCupom inválido ou não utilizado.")
        return total
