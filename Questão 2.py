maior = None

while True:
    n = int(input("Digite um número (0 para sair): "))
    if n == 0:
        break
    if (maior is None) or (n > maior):
        maior = n

if maior is None:
    print("Nenhum número válido foi digitado.")
else:
    print("O maior número digitado foi:", maior)