'''
    Crie um programa que utilize as seguintes operações no banco de dados
    (update, select, delete, insert).
    
'''

import psycopg2

try:
    con  = psycopg2.connect( 
        'host=192.168.1.9 port=5432 dbname=projeto1 user=admin password=louvor01'
    )
    cur = con.cursor()
except Exception as e:
    print("Erro: {}".format(e))
    

try:
    # update
    nome = input("Quem deseja atualizar? ")
    valor = float(input("Qual o novo valor: "))
    cur.execute("update produtos set preco={} where nome='{}'".format(valor, nome))
    # delete
    #delete = input("Que produto deseja ecluir : ")
    #cur.execute("delete from produtos where nome='{}'".format(delete))
    '''
    # insert
    produto = input("Digite o nome do produto : ")
    quantidade = int(input("Informe a quantidade : "))
    valor = float(input("Informe o preço do produto : "))
    cur.execute("insert into produtos (nome, quantidade, preco) values ('{}', {}, {})".format(produto, quantidade, valor))
    '''
    # select
    cur.execute("select * from produtos;")
    print(cur.fetchall())
    
    # persistir registros na base de dados
    con.commit()
    
except Exception as e:
    print('Erro: {} '.format(e))
    con.rollback()
finally:
    cur.close()
    con.close()
    