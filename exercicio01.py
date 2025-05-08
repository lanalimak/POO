from biblioteca import Pessoa

aluno01 = Pessoa("Lana",18,47)
aluno02 = Pessoa("Jess",23,50)
aluno01.nome = "Lana Del Rey"
print(f"{aluno01.nome} tem {aluno01.idade} anos e pesa {aluno01.peso} kg")
aluno02.nome = "Jess Dance"
print(f"{aluno02.nome} tem {aluno02.idade} anos e pesa {aluno02.peso} kg")
aluno01.falar()
aluno01.comer("Pipoca")
aluno01.dormir()