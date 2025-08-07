
from datetime import date

data_hoje = date.today().year

programa = int(input("Insira o seu ano de nascimento. "))

idade =  data_hoje - programa

if idade <18:
    print(f'A sua idade não é suficiente para o recenseamento')
elif idade > 25:
    print(f'Já passou o prazo para o recenseamento')
else:
    print(f'Está na idade ideal para o recenseamento')