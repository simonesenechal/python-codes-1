#Exercicio 23

#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados. 
# Ex: Digite um número: 1834 unidade: 4 dezena: 3 centena: 8 milhar: 1 

number = int(input('Digite um número entre 0 e 9999: '))
unidade = number // 1 % 10
dezena = number // 10 % 10
centena = number // 100 % 10
milhar = number // 1000 % 10

print(f'O número {number} possui {unidade} unidades, {dezena} dezenas, {centena} centena e {milhar} milhar.')






