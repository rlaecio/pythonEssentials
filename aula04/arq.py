#!/usr/bin/python3

with open('frutas.txt', 'r') as arq:
   # arq.write('limão\n')
   # arq.write('melancia\n')
   print(arq.readlines())
'''
    arquivo = open('frutas.txt', 'w')
    arquivo.write('mamao')
    arquivo.close('')
'''
