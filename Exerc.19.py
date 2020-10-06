#Exercicio 19

#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido 

import random

lista = ('Sofia', 'Aurora', 'Rita', 'Ramona' )
choose = random.choice(lista)

print(f'A aluna que vai apagar o quadro é: {choose}')



