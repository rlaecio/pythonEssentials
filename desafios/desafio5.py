'''
    Faça uma abstraçao de uma conta corrente que tenha
    no mínimo 3 métodos(sacar, depositar, transferir)
    instancie a classe poupança herdando de conta conrrente,
    porém deve realizar um método com polimorfismo
    e incrementar o método render juros.
    
'''
class Conta():
    ''' Tentando abstrair uma conta corrente'''
    def __init__(self, titular, numero, saldo):
        self.titular = titular
        self.numero = numero
        self.saldo = saldo
        
    def sacar(self, valor):
        self.saldo -= valor
    
    def depositar(self, valor):
        self.saldo += valor
    
    def transferir(self, valor, conta):
        self.sacar(valor)
        conta.depositar(valor)
        


class Poupanca(Conta):
    def __init__(self, titular, numero, saldo):
        super().__init__(titular, numero, saldo)
        self.juros = 0.005
        
    def reder_juros(self):
        self.saldo += self.saldo * self.juros
        
        
   

c1 = Conta('Daniel', 1234567, 1500)
c2 = Poupanca('Rafael', 3245657, 1500)


c2.sacar(500)
print(c2.saldo, c2.titular, sep='\n')

c1.transferir(500,c2)
c2.reder_juros()
print(c1.saldo, sep='\n')
print(c2.saldo)
