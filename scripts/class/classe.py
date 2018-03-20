

class Pessoa(object):
    def __init__(self, nome):
        self.nome = nome

pessoa_exemplo = Pessoa('Cleber')
print pessoa_exemplo.nome

#mudar o nome da pessoa
pessoa_exemplo.nome = 'Thais'
print pessoa_exemplo.nome
