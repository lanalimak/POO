class Pessoa():
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
        print(f" {self.nome} começou a dormir")