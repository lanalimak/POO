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

class Ingresso():
    def __init__(self, valor):
        self.valor = valor
    def ImprimeValor(self):
        print (f"O valor do ingresso é {self.valor}")

class Vip(Ingresso):
    def __init__(self, valor):
        super().__init__(valor)
    def valorVip(self):
        print (f"O valor VIP é {self.valor+50}")

class Forma():
    def __init__():
        self.area = 0
        self.perimetro = 0

"""class Retangulo (Forma):
    def __init__(self):
    super().__init__()

    def calcularA (self, base, altura):
        self.area = base*altura
        print (f"Área do retângulo é {self.area}")
    def calcularPc(self, base, altura):
        self.perimetro = 2*(base + altura)
        print (f"O perímetro do retângulo é {self.perimetro}")"""

class Atleta:
    def __init__(self, nome, peso):
        self.nome = nome
        self.peso = 0
        self.aposentado = False
        self.aquecer = False

    def testar_participacao(self):
        if self.aposentado:
            print(f"{self.nome} está aposentado.")
        else:
            print(f"{self.nome} pode participar porque não está aposentado.")

    def aquecer(self):
        if self.aposentado:
            print(f"{self.nome} está aposentado.")
        else:
            print(f"{self.nome} pode participar porque não está aposentado.")