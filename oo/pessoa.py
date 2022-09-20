class Pessoa:
    def __init__(self, *filhos, nome=None, idade=30):
        self.idade = idade
        self.nome = nome
        self.filhos =list(filhos)
    def cumprimentar(self):
        return f'oLá {id(self)}'

if __name__ == '__main__':
    pablo = Pessoa(nome='pablo')
    joao = Pessoa(pablo,nome='joao')
    print(Pessoa.cumprimentar(joao))
    print(id(joao))
    print(joao.cumprimentar())
    print(joao.nome)
    print(joao.idade)
    for filhos in joao.filhos:
        print(filhos.nome)
    joao.sobrenome='Ramalho'
    del joao.filhos
    print(joao.__dict__)
    print(pablo.__dict__)