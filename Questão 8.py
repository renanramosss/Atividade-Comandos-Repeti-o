import random

numero_secreto = random.randint(1, 100)

tentativas = 0

print("Tente adivinhar o número entre 1 e 100!")

while True:
    palpite = int(input("Digite seu palpite: "))
    tentativas += 1

    if palpite < numero_secreto:
        print("O número secreto é MAIOR.")
    elif palpite > numero_secreto:
        print("O número secreto é MENOR.")
    else:
        print("Parabéns! Você acertou!")
        break  # sai do loop quando acerta

print(f"Quantidade de tentativas: {tentativas}")

if tentativas <= 5:
    print("Desempenho: Excelente!")
elif tentativas <= 10:
    print("Desempenho: Bom!")
else:
    print("Desempenho: Tente melhorar!")