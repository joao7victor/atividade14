# Exercício Python 14: Escreva um programa que pergunte o salário de um funcionário
# e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um
# aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salário=float(input("digite o salario de um funcionario"))

if salário>1250:
 superior= salário + (salário* 10/100)  
 print(f'Você teve um aumento de 10%. Novo Salario R$ {superior:.2f}')

elif salário <= 1250:
    inferior = salário + (salário * 15 / 100)
    print(f'Você teve um aumento de 15%. Novo Salario R$ {inferior:.2f}')