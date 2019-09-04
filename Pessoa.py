import random
class Pessoa:
    def __init__(self, tipo_grad):
        self.tipo_grad = tipo_grad

    def tipo_grad():
        i=random.uniform(0, 1)
        if i<6.6/100:
            return 'superior de tecnologia'
        else:
            return 'não superior de tecnologia'



class Populacao:
    def _init_(self, tamanho=1000):
        self.tamanho = tamanho
        self.individuos = []
    def amostra(self, n):
        pass

p1=Pessoa(Pessoa.tipo_grad())
print(p1.tipo_grad)
