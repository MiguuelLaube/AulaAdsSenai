class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
    def mostrar_saldo(self):
        print(f"saldo de: {self.saldo}")
    def mostrar_titular(self):
        print(f"Correntista: {self.titular}")

conta = ContaBancaria("Maria", 0)
conta.depositar(5000)
conta.sacar(1000)
conta.mostrar_saldo()
conta.mostrar_titular()
