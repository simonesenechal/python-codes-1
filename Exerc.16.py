#Exercicio 16

#Crie um programa que leia um número Real qualquer pelo teclado e 
# mostre na tela a sua porção Inteira. Ex: Digite um número: 6.127 O número 6.127 
# tem a parte Inteira 6. 

import math

number = float(input('Digite um número: '))
whole = math.trunc(number)

print(f'A parte inteira do número {number} é {whole}')






