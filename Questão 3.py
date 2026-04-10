
menorque21 = 0
maiorque50 = 0

for n in range (10):
    idade = int(input(f"Digite a idade da {n+1}ª pessoa:"))
    
    if idade < 21:
        menorque21 += 1
    elif idade > 50:
          maiorque50 += 1

print("Total de pessoas com menos de 21 é:" , menorque21)
print(f"Total de pessoas com mais de 50 é:" , maiorque50)