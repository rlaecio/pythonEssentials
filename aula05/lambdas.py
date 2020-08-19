#!/usr/bin/python3


''' 
    exemplo 1
    lamb = lambda a, b, c: ((b ** 2) - (4 * a * c))
    print (lamb(3, -2, -5))


    exemplo 2
    a = lambda x, y: x + y
    print(a(5, 6))


    exemplo 3
    print((lambda x: x ** 2) (3))


quadrado = []

for x in range(1, 11):
    quadrado.append((lambda x: x ** 2) (x))
    
print(quadrado)

'''
quadrado = list(map(lambda x: x ** 2, range(1, 11)))

print(quadrado)