#!/usr/bin/python3


def cadastro(**pessoa):
    print('O susuário {} {} foi cadastrado com sucesso!'.format(pessoa['nome'], pessoa['sobrenome']))

cadastro(nome='Daniel', sobrenome='Ferreira', idade=24)

exit()

print('--------------------------------------')

def soma(*num):
    return sum(num)
    
total = soma(6, 7, 8, 9, 10, 52, )
print(total)



