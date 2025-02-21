#módulo E
cupom = ["PIZZA10", "DOCEPIZZA", "PEDEMAIS5"]

def aplicarDesconto(total, pedido):
    while True:
        print("\nVocê tem um cupom de desconto? Digite o código ou pressione ENTER para continuar: ")
        cupomDigitado = input().strip().upper()
        
        if cupomDigitado in cupom:
            if cupomDigitado == "PIZZA10" and total >= 100.00:
                desconto = total * 0.10
            elif cupomDigitado == "DOCEPIZZA" and all(p["pizza"] in ["Chocolate", "Banana", "Brigadeiro", "Romeu e Julieta", "Ouro Branco", "Banoffe", "Brigadeiro Branco"] for p in pedido):
                desconto = total * 0.15
            elif cupomDigitado == "PEDEMAIS5":
                desconto = total * 0.05
            else:
                print("\nCupom não aplicável para este pedido. Tente Novamente.")
                continue
        
            totalComDesconto = total - desconto
            print(f"\nDesconto aplicado: R$ {desconto:.2f}")
            print(f"Total com desconto: R$ {totalComDesconto:.2f}")
            return totalComDesconto
    
        print("\nCupom inválido ou não utilizado.")
        return total
