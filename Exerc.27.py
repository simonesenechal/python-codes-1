#Exercicio 27

#Faça um programa que leia o nome completo de uma pessoa, 
#mostrando em seguida o primeiro e o último nome separadamente. 
#Ex: Ana Maria de Souza primeiro = Ana último = Souza 


name = str(input('Digite seu nome completo: ')).strip()
nome = name.split()
last = nome[len(nome)-1]
first = nome[0]

print(f'Seu primeiro nome é: {first}')
print(f'Seu último nome é: {last}')














