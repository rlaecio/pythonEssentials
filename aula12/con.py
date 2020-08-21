import paramiko

try:
    con = paramiko.SSHClient()
    con.load_system_host_keys()
    con.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    con.connect('192.168.1.9', 
                username='rlaecio',
                password='louvor01')
    
except Exception as e:
    print('Erro: {}',format(e))
    exit()
    