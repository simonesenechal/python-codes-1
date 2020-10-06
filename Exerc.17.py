#Exercicios 17

#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo, 
# calcule o mostre o comprimento da hipotenusa. 

import math

catetooposto = float(input('Digite o cumprimento do cateto oposto:  '))
catetoadj = float(input('Digite o cumprimento do cateto adjacente: '))
hipotenusa = math.hypot(catetoadj,catetooposto)

print(f'Cateto oposto: {catetooposto}, Cateto adjacente: {catetoadj} e a hipotenusa: {hipotenusa:.2f}')





