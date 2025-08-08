altura = int(input("Insira a sua altura(em m): "))
peso = int(input("Agora insira o seu peso(em kg): "))

IMC = peso / (altura**2)
if IMC < 18.5:
    print(f'Está abaixo do peso')
elif 18.5 < IMC < 25:
    print(f'Peso normal')
else:
    print(f'Sobrepeso')