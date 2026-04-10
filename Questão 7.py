temperatura=int(input('Digite a temperatura(digite "999" para parar): '))

acima30_temp=0
abaixo15_temp=0
total_temp=0
soma_temp=0

while temperatura != 999:
    total_temp +=1
    soma_temp += temperatura
    if temperatura >=30:
        acima30_temp +=1
    if temperatura <=15:
        abaixo15_temp +=1
    temperatura=int(input('Digite a temperatura(digite "999" para parar): '))
if total_temp > 0:
    media_temp = soma_temp / total_temp
else:
    media_temp = 0

print(f'''Ao total, foram registradas {total_temp} temperaturas
A média de temperaturas é de {media_temp:.2f}
Existem {acima30_temp} temperaturas acima de 30     
Existem {abaixo15_temp} temperaturas abaixo de 15''')
