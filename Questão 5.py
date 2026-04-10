votos = {1: 0, 2: 0, 3: 0}

print('Votação para o representante da turma!')
print('Candidatos: 1 -> Candidato A, 2 -> Candidato B, 3 -> Candidato C')
print('Se quiser que pare a votação, digite "0"')

while True:
    try:
        voto = int(input('Digite o número do candidato que deseja votar: '))
    except ValueError:
        print('Por favor, digite um número válido!')
        continue

    if voto == 0:
        break

    if voto in votos:
        votos[voto] += 1
    else:
        print('Este número não corresponde a nenhum candidato!')

total_validos = sum(votos.values())
vencedor_num = max(votos, key=votos.get)
vencedor_nome = {1: "Candidato A", 2: "Candidato B", 3: "Candidato C"}[vencedor_num]

print("\nResultado da votação:")
print(f"Candidato A: {votos[1]} voto(s)")
print(f"Candidato B: {votos[2]} voto(s)")
print(f"Candidato C: {votos[3]} voto(s)")
print(f"Total de votos válidos: {total_validos}")
print(f"Candidato vencedor: {vencedor_nome}")