#Exercicio 32

#Faça um programa que leia um ano qualquer e mostre se ele é bissexto 

ano = int(input('Escolha um ano: '))

print(' ')

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'Esse ano é Bissexto!')
else:
    print(f'Esse ano não é Bissexto!')


