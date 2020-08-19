#!/usr/bin/python3

produtos = [
    {'nome': 'produto1', 'valor': 2.0},
    {'nome': 'produto2', 'valor': 1.0},
    {'nome': 'produto3', 'valor': 2.5},
    {'nome': 'produto4', 'valor': 3.0},
]


try:
    for produto in produtos:
        produto['valor'] += produto['valor'] * 0.1        
except Exception:
    pass
finally:
    print(produtos)