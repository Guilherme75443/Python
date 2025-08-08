import random

caixa  = int(input("Quanto dinheiro quer levantar(apenas múltiplos de 5 permitidos): "))

print(f'Escolha o tipo de nota{5,10,20,50,100}:')
print(f'Quantas notas quer levantar:')

if caixa != 5*random.randint(1,1000000):
    print(f'Erro!')