#Programa de votação


#Inicializar contagem de votos
votos_ana = 0
votos_carla = 0
(votos_bruno) = 0
print("VOTAÇÁO REALITY SHOW")
print("1--Ana")
print("2--Bruno")
print("3--Carla")
print("0--Encerrar votação")
while True:
    voto = int(input("Digite o número do seu candidato: "))
    if voto == 1:
        votos_ana += 1
    elif voto == 2:
        votos_bruno += 2
    elif voto == 3:
        votos_carla += 3
    else:
        print("Votação encerrada")
        break
print(f'Ana teve {votos_ana} votos')
print(f'Bruno teve {votos_bruno}')
print(f'A Carla teve {votos_carla}')