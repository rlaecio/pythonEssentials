#!/usr/bin/python3

cont = 0
while cont < 100:
    print('Execuçao {}'.format(cont))
    if cont == 10:
        print('interrompendo o loop com break')
        break
    cont += 1