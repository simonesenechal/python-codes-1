#Exercicio 04

#Faça um programa que leia algo pelo teclado e 
#mostre na tela o seu tipo primitivo e todas a s informações possíveis sobre ele.

teste = input('Digite algo: ')

print('O tipo primitivo é:', type(teste))
print('Está em letras maiusculas:', teste.isupper())
print('É alfabeto: ', teste.isalpha())
print('É um número decimal: ', teste.isdecimal())
print('É um título: ', teste.istitle())
print('É númerico: ', teste.isnumeric())
print('Esta em letras minusculas: ', teste.islower())
print('É alfanúmerico: ', teste.isalnum())
print('É um digíto: ', teste.isdigit())







