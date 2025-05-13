"""class Pessoa():
    def __init__(self, nome, idade, peso):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.comendo=False
        self.dormindo=False
        self.falando=False
    def dormir(self):
        if self.dormindo == True:
            print(f" {self.nome} está dormindo.")
        elif
        print(f" {self.nome} não pode dormir porque está falando")
    def comer(self, comida):
        if self.comendo == True:
            print("não pode comer, pois, já está comendo")
        print(f" foi comer {comida}")
    def dormir(self):
        if self.dormindo == True:
            print(f" {self.nome} já está dormindo.")
        print(f" {self.nome} começou a dormir")"""f""

"""class Banco():
    def __init__(self, numero, saldo, nome, tipo, status):
        self.numero = numero
        self.saldo = saldo
        self.nome = nome
        self.tipo = tipo
        self. status = status
    def atvConta
        if"""

     #HERANÇA:
class Animal():
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor
    def comer(self):
        print(f" O {self.nome} foi comer...")

class Cachorro(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)
    def latir(self):
        print(f" {self.nome} está látindo...")

class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)
    def miar(self):
        print(f" {self.nome} está miando...")

class Coelho(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)
    def guinchar(self):
        print(f" {self.nome} está guinchando..")

class Vaca(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)
    def mugir(self):
        print(f" {self.nome} está mugindo...")

class Ingresso()
    def __init__(self, valor, vip):
        self.valor = valor
        self.vip = vip
    def comprar
        super().__init__(valor, vip)