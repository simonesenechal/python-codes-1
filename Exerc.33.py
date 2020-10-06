#Exercicio 33

#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.


num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))
num3 = int(input('Terceiro número: '))

print(f'Os números foram: {num1, num2, num3}')

print(' ')

if num1 < num2 and num1 < num3:
    print(f'O número {num1} é o menor.')
if num2 < num1 and num2 < num3:
    print(f'O número {num2} é o menor.')
if num3 < num1 and num3 < num2:
  print(f'O número {num3} é o menor.')

if num1 > num2 and num1 > num3:
    print(f'O número {num1} é o maior.')
if num2 > num1 and num2 > num3:
    print(f'O número {num2} é o maior.')
if num3 > num1 and num3 > num2:
  print(f'O número {num3} é o maior.')

