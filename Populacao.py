import random
import Pessoa
class Populacao:
    def __init__(self, tamanho=1000):
        self.tamanho = tamanho
        self.individuos = [Pessoa.Pessoa(Populacao.tipo_grad(), Populacao.rede_ensino(), Populacao.modalidade(),
                               Populacao.dif_frequencia(), Populacao.sexo(), Populacao.cor(),
                               Populacao.rendimento_percapita()) for i in range(tamanho)]

    def amostra(self, N):
        return random.sample(self.individuos, N)
    def tipo_grad():
        cv1=(3.7)/100
        j=random.uniform(477*(1-cv1),477*(1+cv1))
        m=random.uniform(0,7242)
        if m<=j:
            return 'superior de tecnologia'
        else:
            return 'não superior de tecnologia'
    def sexo():
        cv1 = (1.7)/100
        j = random.uniform(3118*(1-cv1), 3118*(1+cv1))
        m = random.uniform(0, 7288)
        if m <= j:
            return 'Homem'
        else:
            return 'Mulher'
    def cor():
        cv1 = (1.7)/100
        j = random.uniform(4154*(1-cv1), 4154*(1+cv1))
        m = random.uniform(0, 7288)
        if m <= j:
            return 'Branca'
        else:
            return 'Preta ou Parda'
    def rede_ensino():
        cv1 = (91.)/100
        j = random.uniform(105*(1-cv1), 105*(1+cv1))
        m = random.uniform(0, 477)
        if m <= j:
            return 'pública'
        else:
            return 'particular'
    def modalidade():
        cv1 = (1.8)/100
        j = random.uniform(392*(1-cv1), 392*(1+cv1))
        m = random.uniform(0, 477)
        if m <= j:
            return 'Presencial'
        else:
            return 'À Distância'
    def dif_frequencia():
        cv1 = (8.6)/100
        j = random.uniform(97*(1-cv1), 97*(1+cv1))
        m = random.uniform(0, 477)
        if m <= j:
            return 'Havia'
        else:
            return 'Não Havia'


    def rendimento_percapita():
        #definindo as strings das faixas salariais para facilitar posterior uso
        A="Mais de 5 salários mínimos"
        B="Mais de 3 a 5 salários mínimos"
        C="Mais de 2 a 3 salários mínimos"
        D="Mais de 1 a 2 salários mínimos"
        E="Mais de 1/2 a 1 salário mínimo"
        F="Sem rendimento a 1/2 salário mínimo"
         # não consideramos aqui a faixa "Sem declaração"

        #p_F = nº de pessoas da faixa F
        #cv_F = coeficiente de variação percentual da faixa F
        p_F = 472
        p_E = 1442
        p_D = 2551
        p_C = 1176
        p_B = 745
        p_A = 496

        cv_F = 16.8/100
        cv_E = 8.2/100
        cv_D = 5.2/100
        cv_C = 8.4/100
        cv_B = 10.9/100
        cv_A = 16.7/100

        j_F=random.uniform(p_F-cv_F*p_F,p_F*(1+cv_F)) #colocar p_F em evidência ou multiplicar direto é equivalente
        j_E=random.uniform(p_E*(1-cv_E),p_E*(1+cv_E))
        j_D=random.uniform(p_D*(1-cv_D),p_D*(1+cv_D))
        j_C=random.uniform(p_C*(1-cv_C),p_C*(1+cv_C))
        j_B=random.uniform(p_B*(1-cv_B),p_B*(1+cv_B))
        j_A=random.uniform(p_A*(1-cv_A),p_A*(1+cv_A))
        vetor_j=[j_F,j_E,j_D,j_C,j_B,j_A]
        m=random.uniform(0,sum(vetor_j))
        if m <= sum(vetor_j[:1]):
            return F
        elif m <= sum(vetor_j[:2]):
            return E
        elif m <= sum(vetor_j[:3]):
            return D
        elif m <= sum(vetor_j[:4]):
            return C
        elif m <= sum(vetor_j[:5]):
            return B
        else:
            return A

