#!/usr/bin/python3

idade = int(input("Digite a sua idade: "))
habilitacao = input("Voce é habilitado? ")
dirigir = False


if habilitacao.lower().strip() == 'sim':
    habilitacao = True
else:
    instrutor = input('Voce esta acompanhado de um instrutor? ')
    if instrutor.lower().strip() == 'sim':
        dirigir = True

if idade >= 18 and habilitacao == True:
    print('Voce pode dirigir')
elif dirigir:
    print('Boa aula! ')
else:
    print('Voce não pode difrigir')
    
