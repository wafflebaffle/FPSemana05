class ContaBancaria:

    def __init__(self, titular, credit, limit):
        self.titular = str(titular)
        self.credit = float(credit)
        self.limit = float(limit)

    def depositar(self,value):
        if value >= 0:
            self.credit += value
            print(1)
        else:
            print(0)
    
    def levantar(self,value):
        if value >= self.credit+self.limit:
            print(0)
        else:
            self.credit-=value
            print(1)
    
    def exibir_info(self):
        print(f'{self.titular} {(self.credit):.2f} {(self.limit):.2f}')


conta = ContaBancaria("João", 1000.00, 500.00)
conta.depositar(-500.00)
conta.depositar(500.00)
conta.levantar(1200.00)
conta.levantar(1200.00)
conta.exibir_info()
