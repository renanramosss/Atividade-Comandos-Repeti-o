while True: 

    valor1 = float(input("Digite o primeiro valor: "))

    valor2 = float(input("Digite o segundo valor: "))

    soma = valor1 + valor2

    print("Soma:", soma)

    resposta = input("Novo cálculo (S/N)? ")

    resposta = resposta.upper()

    if resposta == "N":
        print("Fim dos Cálculos")
        break  

