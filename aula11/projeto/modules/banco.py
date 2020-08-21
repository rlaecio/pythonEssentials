from pymongo import MongoClient, DESCENDING
import time

try:
    con = MongoClient()
    db = con['chat']
except Exception as e:
    print('ERRO: {}'.format(e))
    exit()
    
def cadastrar_mensagem(nome, mensagem):
    date = {
        'nome': nome,
        'mensagem': mensagem,
        'hora': time.strftime('%d-%m-%Y %H:%M:%S')
    }
    
    db.chat.insert(date)
    
def busca_mensagem():
    ultimo = [ x for x in db.chat.bind().sort('_id', DESCENDING)]
    while True:
        date = [ x for x in db.chat.bind().sort('_id', DESCENDING)]
        if date != ultimo:
            print("[{}] {} : {} \n".format(
                date[0]['hora'], date[0]['nome'], date[0]['mensagem']
            ))
        time.sleep(2)
        
    
    
    