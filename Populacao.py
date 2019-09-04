class Populacao:
    def _init_(self, tamanho=1000):
        self.tamanho = tamanho
        self.individuos = []
    def amostra(self, n):
        pass

p1=Pessoa(Pessoa.tipo_grad())
print(p1.tipo_grad)
print("testando push de novo")