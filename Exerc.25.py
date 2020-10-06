# Exercicio 25

#Crie um programa que leia o nome de uma pessoa e diga se ela tem ‘SILVA’ no nome. 

name = str(input('Digite seu nome completo: ')).strip().lower()

procura = 'silva' in name 

print(f'O nome contém a palavra Silva? {procura}')



