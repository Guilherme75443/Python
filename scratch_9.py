n  = int(input("Quantidade de kWh consumida?: "))

x = input("Qual é o  tipo de instalação?: ")

if  x == "R":
    if rWh > 500:
        print(f'O valor pago é {n*0.65}')
    else:
         print(f'O valor pago é ')
if x == "C":
    if cWh >1000:
        print(f'O valor pago é {n*0.60}')
if x == "I":
    if iWh >5000:
        print(f'O vaor pag é {n*0.60}')