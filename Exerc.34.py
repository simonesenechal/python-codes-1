#Exercicio 34

#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
# Para salários superiores a R$ 1.250,00, 
# calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%. 


salary = float(input('Salário do funcionário: '))
limit = 1250
superior = salary * 0.10
inferior = salary * 0.15

if salary <= limit:
    print(f'O valor do aumento do salário é de R${inferior:.2f}, novo salário: R${salary + inferior:.2f}')
else: 
    print(f'O valor do aumento do salário é de R${superior:.2f}, novo salário: R${salary + superior:.2f}')




