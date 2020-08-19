#!/usr/bin/python3

'''
2 - Faça um programa que leia 4 notas de um aluno e calcule a média 
e faça a seguinte validaçao nota igual ou maior que 7 aprovado,
notas menor que 7 e maior que 3 recuperaçao e 
notas menores ou igual a 3 reprovado.

'''

try:
    for x in range(4):
        soma = 0
        nota = int(input("Digite nota{}: ".format(x+1)))
        if nota > 10:
            raise ValueError('Não existe nota superior que 10')
        soma += nota

except ValueError as e:
    print(e)

media = soma / 4

if media >= 7:
    print('Media {}, aprovado!'.format(media))
elif media > 3:
    print('Media {}, recuperação'.format(media))
else:
    print('Media {}, reprovado'.format(media))
