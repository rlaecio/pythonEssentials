from core import user_table, engine

con = engine.connect()
ins = user_table.insert()

#new = ins.values(idade=24, nome='Daniel', senha='teste123')
#con.execute(new)

con.execute(ins, [
    {'nome': 'João', 'idade': 38, 'senha': 'senha123'},
    {'nome': 'Maria', 'idade': 45, 'senha': 'senha1234'},
    {'nome': 'Gustavo', 'idade': 28, 'senha': 'senha12345'},
    
])