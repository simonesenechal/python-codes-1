#Exercicio 28

#Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. 
# O programa deverá escrever na tela se o usuário venceu ou perdeu. 


import random 

computer = random.randint(0,5)
user = int(input('Qual o número escolhido pelo o computador? '))

print(' ')

print(f'O número escolhido pelo o computador foi: {computer}')

print(' ')
if computer == user:
    print(f'PARABÉNS!!! Você acertou!')
else:
    print(f'ERROU!!! Não foi dessa vez, tente novamente!')




