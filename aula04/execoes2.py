#!/usr/bin/python3

num = input('Digite um numero: ')


try:
    if num.isnumeric():
        print(int(num) + 2)
        
except Exception:   
    print('num não é um numero! ')
