#Exercicios 13

#Faça um algoritmo que leia o salário de uma funcionário e mostre seu novo salário, com 15% de aumento 

salary = float(input('Qual o salário do funcionário? '))
increase = salary * 0.15
newsalary = salary + increase

print(f'O antigo salário do funcionário é de {salary} com o aumento de 15% o novo salário é de R${newsalary}')


