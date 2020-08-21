from pymongo import MongoClient
from pprint import pprint

try:
   con = MongoClient('mongodb://192.168.1.9:27017/')
   db = con['projeto1']
except Exception as e:
   print("Erro: {}".format(e))
   exit()

## - ex1:
#db.users.insert_one({'_id':2, 'nome': 'Pedro', 'idade': 40 })
#print(db.users.find_one()['nome'])

## - ex2:
#for x in db.users.find():
#   print(x)

## - ex3:
#db.users.delete_one( { '_id':2} )

## - ex4:
#db.users.update_one( {'_id':3}, {'$set': {'projetos': []}} )

## - ex5:
db.users.update_one( {'_id':3}, {'$push': {'projetos': {'nome': 'bevops2', 'desc': 'api2'}}} )
pprint([x for x in db.users.find()])
