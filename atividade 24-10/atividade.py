class Contato:
    def __init__(self, tipo:str, contato:str) -> None:
        self.tipo = tipo
        self.contato = contato

class cliente:
    def __init__(self, nome:str) -> None:
        self.nome = nome
        self.contatos = []
        self.conta = None
    def criar_conta(self):
        self.conta = conta(self.nome)
    def add_contato(self):
        tipo = input('informe o tipo: ')
        ctt = input('informe o contato: ')
        self.contatos.append(Contato(tipo, ctt))
    def ver_contatos(self):
        for c in self.contatos:
            print(f'{c.tipo}: {c.contato}')    

class conta:
    def __init__(self, titular:str, agencia:int, num_conta:int) -> None:
        self.titular = titular
        self.num_conta = num_conta
        self.saldo = 00
        self.chave_pix = []
        self.agencia = agencia
    def transferir(self, conta_alvo, valor):
        if valor > self.__saldo:
            print('saldo insuficiente')
        else:
            self.__saldo -= valor * 1.02
            conta_alvo.__saldo += valor 
    def depositar(self, valor):
        self.saldo += valor
    def ver_saldo(self):
        return self.saldo
    def adicionar_pix(self, chave):
        self.chave_pix.append(chave)



