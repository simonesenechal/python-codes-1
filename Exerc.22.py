#Exercicio 22

# Crie um programa que leia o nome completo de uma pessoa e mostre: 
# O nome com todas as letras maiúsculas e minúsculas. 
# Quantas letras ao todo (sem considerar espaços) 
# Quantas letras tem o primeiro nome. 

nome = str(input('Qual seu nome completo? ')).strip()

total = len(nome) - nome.count(' ')
primeiro = nome.find(' ')
separa = nome.split()
separa1 = separa[0]
separa2 = len(separa[0])

print(' ')
print('Analisando seu nome...')
print(' ')

print(f'Seu nome em letras maiúsculas é: {nome.upper()}')
print(f'Seu nome em letras minúsculas é: {nome.lower()}')
print(f'Seu nome tem ao todo: {total}')
print(f'Seu primeiro nome tem {primeiro}')
print(f'Seu primeiro nome é {separa1} e ele possui {separa2} letras. ')










