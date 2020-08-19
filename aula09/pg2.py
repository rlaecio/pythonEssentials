import psycopg2

try:
    con  = psycopg2.connect( 
        'host=192.168.1.9 port=5432 dbname=projeto1 user=admin password=louvor01')
    cur = con.cursor()
except Exception as e:
    print('Erro : {}'.format(e))
    exit()
    
#cur.execute("insert into usuarios (nome, idade) values ('Pedro', 25);") # -> insert
#con.commit()

#cur.execute("update usuarios set idade=37 where id=5;")   # -> update 
#con.commit()

#cur.execute("delete from  usuarios where id=2;")   # ->  delete
#con.commit()

cur.execute("select * from  usuarios")   # ->  select
print(cur.fetchone()) # -> apresenta o primeiro item 

print(cur.fetchall()) # -> traz todos os registros

cur.close()
con.close()