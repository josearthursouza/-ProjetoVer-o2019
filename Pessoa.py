import random
class Pessoa:
    def __init__(self, tipo_grad,rede_ensino,modalidade,dif_frequencia,sexo,cor,rendimento_percapita,):
        self.tipo_grad = tipo_grad
        self.rede_ensino = rede_ensino
        self.modalidade = modalidade
        self.dif_frequencia = dif_frequencia
        self.sexo = sexo
        self.cor = cor
        self.rendimento_percapita = rendimento_percapita


p1=Pessoa("não superior")
print(p1.tipo_grad)






