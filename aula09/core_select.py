from  sqlalchemy import select
from core import user_table

#result = select([user_table])
#result = select([user_table]).where(user_table.c.nome == 'Daniel Prata')

#for x in result.execute():
#    print(x)


#print([x for x in result.execute()])
print([x for x in select([user_table]).where(user_table.c.nome == 'Daniel Prata').execute()])