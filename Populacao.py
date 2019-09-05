
import random
import Pessoa
class Populacao:
    def _init_(self, tamanho=1000):
        self.tamanho = tamanho
        #self.individuos = []
        o=[]
        for i in range(tamanho):
            p2 = Pessoa.Pessoa(Populacao.tipo_grad(), Populacao.rede_ensino(), Populacao.modalidade(),
                               Populacao.dif_frequencia(), Populacao.sexo(), Populacao.cor(),
                               Populacao.rendimento_percapita())
            #for j in [p2.tipo_grad, p2.rede_ensino, p2.modalidade, p2.dif_frequencia, p2.sexo, p2.cor,
                      #p2.rendimento_percapita]:
                #individuos.append(j)
            self.o.append(p2)
        self.individuos=o
        ########## PRECISA MUDAR ISS AQUI
    def amostra(self, N):
        return rm.choice(self.individuos, N)
    def tipo_grad():
        #desvpad=cv*media
        dv1=(3.7)/100
        j=random.uniform(477*(1-dv1),477*(1+dv1))
        m=random.uniform(0,7242)
        if m<=j:
            return 'superior de tecnologia'
        else:
            return 'não superior de tecnologia'
    def sexo():
        dv1 = (1.7)/100
        j = random.uniform(3118*(1-dv1), 3118*(1+dv1))
        m = random.uniform(0, 7288)
        if m <= j:
            return 'homem'
        else:
            return 'mulher'
    def cor():
        dv1 = (1.7)/100
        j = random.uniform(4154*(1-dv1), 4154*(1+dv1))
        m = random.uniform(0, 7288)
        if m <= j:
            return 'branca'
        else:
            return 'preta ou parda'
    def rede_ensino():
        dv1 = (91.)/100
        j = random.uniform(105*(1-dv1), 105*(1+dv1))
        m = random.uniform(0, 477)
        if m <= j:
            return 'pública'
        else:
            return 'particular'
    def modalidade():
        dv1 = (1.8)/100
        j = random.uniform(392*(1-dv1), 392*(1+dv1))
        m = random.uniform(0, 477)
        if m <= j:
            return 'presencial'
        else:
            return 'a distância'
    def dif_frequencia():
        dv1 = (8.6)/100
        j = random.uniform(97*(1-dv1), 97*(1+dv1))
        m = random.uniform(0, 477)
        if m <= j:
            return 'havia'
        else:
            return 'não havia'

            
##############by Rener### apagar isso depois - apenas para marcar a funcao criada         
#Definindo o parâmetro rendimento_percapita
    def rendimento_percapita():
        #copiando dados de rendimento per capita da tabela
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
        
        #Gerando os intervalos com os erros
        #A ideia é jogar um dado e definir a renda da pessoa de acordo com o que sair nesse dado
        #Porém o dado não é uniforme e a probabilidade de cada item não é 1/6
        #A probabilidade da pessoa ter uma determinada renda, será dada pela proporção da planilha mais ou menos um erro
        #esses erros são os coeficientes de variacao em percentual multiplicados pelo valor absoluto da população pertencente àquela classe segunda a planilha
        #Assim, pense no sorteio do dado como um sorteio de um ponto em uma reta numerada de zero até a população total - considerando os erros
        #O que definirá  a renda da pessoa em qual ponto dessa reta caiu o sorteado, sendo que as proporções calculadas gerarão os intervalos necessários

        e_F=random.uniform(p_F-cv_F*p_F,p_F*(1+cv_F)) #colocar p_F em evidência ou multiplicar direto é equivalente
        e_E=random.uniform(p_E*(1-cv_E),p_E*(1+cv_E))
        e_D=random.uniform(p_D*(1-cv_D),p_D*(1+cv_D))
        e_C=random.uniform(p_C*(1-cv_C),p_C*(1+cv_C))
        e_B=random.uniform(p_B*(1-cv_B),p_B*(1+cv_B))
        e_A=random.uniform(p_A*(1-cv_A),p_A*(1+cv_A))
        vetor_e=[e_F,e_E,e_D,e_C,e_B,e_A]
        k = sum(vetor_e)  
        m=random.uniform(0,k)
        if m <= sum(vetor_e[:1]):
            return F
        elif m <= sum(vetor_e[:2]):
            return E
        elif m <= sum(vetor_e[:3]):
            return D
        elif m <= sum(vetor_e[:4]):
            return C
        elif m <= sum(vetor_e[:5]):
            return B
        else:
            return A     
##############by Rener### apagar isso depois - apenas para marcar a funcao criada
Brasil=Populacao
Brasil.individuos()