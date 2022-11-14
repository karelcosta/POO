class Contato:
    def __init__(self, tipo:str, contato:str) -> None:
        self.tipo = tipo
        self.contato = contato

class cliente:
    def __init__(self, nome:str) -> None:
        self.nome = nome
        self.contatos = []
        self.conta = None
    def criar_conta(self, tipo, agencia, nunconta):
        if tipo==1:
            self.conta = conta(self.nome, agencia, nunconta)
        elif tipo==2:
            self.conta = conta_corrente(self.nome, agencia, nunconta)
        elif tipo==3:
            self.conta = conta_polpança(self.nome, agencia, nunconta)
    def add_contato(self, tipo:str, ctt):
        self.contatos.append(Contato(tipo, ctt))
    def ver_contatos(self):
        for c in self.contatos:
            print(f'{c.tipo}: {c.contato}')    

class chave_pix:
    def __init__(self, chave) -> None:
        self.chave = chave

class conta:
    def __init__(self, titular:str, agencia:int, num_conta:int):
        self.titular = titular
        self.num_conta = num_conta
        self.saldo = 00
        self.chave_pix = None
        self.agencia = agencia
    def transferencia(self, conta_alvo, valor):
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
        self.chave_pix = chave_pix(chave)

class conta_corrente(conta):
    def transferencia(self, conta_alvo, valor):
        if valor > self.__saldo:
            print('saldo insuficiente')
        else:
            self.__saldo -= valor * 1.10
            conta_alvo.__saldo += valor

class conta_polpança(conta):
    def transferencia(self, conta_alvo, valor):
        if valor > self.__saldo:
            print('saldo insuficiente')
        else:
            self.__saldo -= valor * 1.005
            conta_alvo.__saldo += valor

# criando os clientes 
c1 = cliente('usuario 1')    
c2 = cliente('usuario 2')
c3 = cliente('usuario 3')
#criando a conta para os clientes
#conta normal
c1.criar_conta(1, 'caixa', 100001)
#conta corrente
c2.criar_conta(2, 'brasil', 144671)
#conta polpança
c3.criar_conta(3, 'bradesco', 235604)
#criando contatos para os clientes
c1.add_contato('trabalho', 99984654534)
c2.add_contato('pessoal', 99982867495)
c3.add_contato('trabalho', 99985463412)
#adicionando chaves pix
c1.conta.adicionar_pix('99984654534')
c2.conta.adicionar_pix('09867523419')
c3.conta.adicionar_pix('usuario3@gmail.com')
#printando chaves pix

print(f'{c1.nome}: {c1.conta.chave_pix.chave}')
print(f'{c2.nome}: {c2.conta.chave_pix.chave}')
print(f'{c3.nome}: {c3.conta.chave_pix.chave}')

