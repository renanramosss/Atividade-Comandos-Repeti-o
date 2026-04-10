total = 0
quantidade = 0

while True:
    venda = float(input("Digite o valor da venda (0 para encerrar): "))
    
    if venda == 0:
        break
    
    total += venda
    quantidade += 1

# Verificação para evitar divisão por zero
if quantidade > 0:
    media = total / quantidade
else:
    media = 0

print("\nResultado do dia:")
print("Total vendido:", total)
print("Quantidade de vendas:", quantidade)
print("Média das vendas:", media)