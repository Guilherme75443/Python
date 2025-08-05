radar = int(input("Qual é a velocidade do carro?"))
if radar > 80:
    extra = radar - 80
    multa = extra * 2
    print(multa)

if radar <= 80:
    print("Sem multa")
