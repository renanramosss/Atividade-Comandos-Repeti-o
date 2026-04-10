# Questão 10 - Controle de Estoque

estoque = int(input("Digite a quantidade inicial em estoque: "))

while estoque > 0:
    venda = int(input("Quantidade vendida (0 para encerrar): "))

    if venda == 0:
        break

    estoque -= venda

    print("Estoque atual:", estoque)

    if estoque < 10 and estoque > 0:
        print("Estoque baixo! Repor imediatamente.")

    if estoque <= 0:
        print("Estoque zerado. Programa encerrado.")
        break
