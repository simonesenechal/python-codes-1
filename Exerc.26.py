#Exercicio 26

#Faça um programa que leia uma frase pelo teclado e mostre: Quantas vezes aparece a letra ‘A’ 
# Em que posição ela aparece a primeira vez Em que posição ela aparece a última vez  


frase = str(input('Escreva uma frase: ')).strip().lower()
quantidade = frase.count('a')
first = frase.find('a') + 1 
last = frase.rfind('a') + 1

print(f'A letra A aparece {quantidade} vezes na frase.')
print(f'A letra aparece na posição {first} na primeira vez.')
print(f'A letra aparece na posição {last} na última vez.')




