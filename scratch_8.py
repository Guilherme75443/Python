x = int(input("Qual é o salario atual?: "))

if x <500:
             print(f'O seu salario recebe um aumento de 15%,logo será {x+(x*0.15)}')
elif x <1000:
             print(f'O seu salario recebe um aumento de 10%,logo será {x+(x*0.10)}')
else:
             print(f'O seu salario recebe um aumento de 5%,ogo será {x+(x*0.05)}')


