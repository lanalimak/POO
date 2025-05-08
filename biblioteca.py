class Pessoa():
    def _init_(self, nome, idade, peso):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.comendo=False
        self.dormindo=False
        self.falando=False
    def falar(self):
        if self.falando == True:
            print("nao pode falar pois ja esta falando")
        print(f" {self.nome} começou a falar ")
    def comer(self, comida):
        if self.comendo == True:
            print("nao pode comer pois ja esta comendo")
        print(f" foi comer {comida}")
    def dormir(self):
        if self.dormindo == True:
            print("nao pode dormir pois ja esta dormindo")
        print(f" {self.nome} começou a dormir")