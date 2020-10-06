#Exercicio 18

#Faça um programa que leia um ângulo qualquer a 
# mostre na tela o valor do seno, cosseno e tangente desse ângulo. 

import math

angulo = float(input('Qual o angulo que deseja: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print(f'Em um ângulo de {angulo}º o seno é {seno:.2f}, cosseno {cosseno:.2f} e a tangente {tangente:.2f}')



