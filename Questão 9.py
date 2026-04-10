# Questão 9 - Análise de Clientes

total_salario = 0
maior_idade = 0
menor_idade = 999
feminino_acima_3000 = 0
acima_50 = 0

for i in range(1, 21):
    print(f"\nCliente {i}")
    
    idade = int(input("Idade: "))
    sexo = input("Sexo (M/F): ").upper()
    salario = float(input("Salário: "))

    total_salario += salario

    if idade > maior_idade:
        maior_idade = idade

    if idade < menor_idade:
        menor_idade = idade

    if sexo == "F" and salario > 3000:
        feminino_acima_3000 += 1

    if idade > 50:
        acima_50 += 1

media = total_salario / 20
percentual = (acima_50 / 20) * 100

print("\n--- RESULTADO ---")
print("Média salarial:", media)
print("Maior idade:", maior_idade)
print("Menor idade:", menor_idade)
print("Mulheres com salário acima de 3000:", feminino_acima_3000)
print("Percentual com idade acima de 50:", percentual, "%")
