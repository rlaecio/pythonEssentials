#!/usr/bin/python3

ling  = input("digite a melhor linguagem de programação: ")
try:
    if ling.lower().strip() == 'python':
        print('Você acertou')
    else:
        raise ValueError('\nLinguagem errada!')
    
except ValueError   as e:
    print("ERRO: {}".format(e))