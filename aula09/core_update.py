from sqlalchemy import update
from core import user_table, engine

con = engine.connect()

atualizar = update(user_table).where(user_table.c.nome == 'João')
commit = atualizar.values(nome='António')

result = con.execute(commit)
print(result.rowcount)
