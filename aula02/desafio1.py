#!/usr/bin/python3
'''
    1. Calcular a soma das diagonais de uma matriz 
    matriz = [
        [1,2,3],
        [2,5,6],
        [7,8,9]
    ]
exemplo = 1+5+9+3+5+7
'''

matriz = [
    [10, 2, 8],
    [40, 5, 6],
    [10, 8, 9]
]
a, b = 0, 0

for x, y in enumerate(matriz):
    a += y[x]
    b += y[-(x+1)]
print(a + b)
    
    