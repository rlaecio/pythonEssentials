import pymysql

try:
    con = pymysql.connect('192.168.1.9', 'admin', 'louvor01', 'projeto1')
    
    cur = con.cursor()
    
except Exception as e:
    print('Erro: {}'.format(e))
    exit
    
## - ex1:    
#cur.execute("insert into clientes(nome, endereco) values ('Roque Laecio', 'Portugal');")
#con.commit()

## - ex2:
#cur.execute("update clientes set endereco='United Kingdom' where id=1;")
#con.commit()

## - ex3:
#cur.execute("delete from clientes where id=1;")
#con.commit()

## -ex4:
cur.execute("select * from clientes;")

## print first 
#print(cur.fetchone())

## print all
print(cur.fetchall()[0][1])

cur.close()
con.close()
