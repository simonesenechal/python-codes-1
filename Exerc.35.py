#Exercicio 35

#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário 
# se elas podem ou não formar um triângulo.

reta1 = int(input('Digite o cumprimento da primeira reta: '))
reta2 = int(input('Digite o cumprimento da segunda reta: '))
reta3 = int(input('Digite o cumprimento da terceira reta: '))


if (reta1 + reta2) > reta3 and (reta1 + reta3 ) > reta2 and (reta2 + reta3) > reta1:
    print(f'Neste caso podemos formar um triângulo.')
else:
    print(f'Não formamos um triângulo com essas medidas.')
    

