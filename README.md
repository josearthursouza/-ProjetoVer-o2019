## ProjetoVerao2019 - Descrição

Neste arquivo se encontra a descrição do projeto desenvolvido por __José Arthur__ e __Rener Oliveira__, que se trata de um simulador de população que se baseia nos dados da PNAD/IBGE 2014 para gerar os atributos que serão descritos posteriormente, tentando se aproximar dos valores de média e variação dos dados oficiais.
### Classe Pessoa
A classe Pessoa, do arquivo [Pessoa.py](https://github.com/josearthursouza/ProjetoVerao2019/blob/master/Pessoa.py), foi usada para caracterizar os atributos que julgamos relevantes dentre os vários da PNAD, focando naqueles mais relacionados com a situação socio-educacional dos pesquisados.
No total, foram 7, sendo eles:
- _Tipo de Gradução:_ Tecnológica ou não-tecnológica
- _Rede de Ensino:_ Pública ou particular
- _Modalidade de ensino_: Presencial ou à distância
- _Dificuldade de frequentar as aulas_: Possuía ou não possuía
- _Sexo:_ Masculino ou Feminino
- _Cor_: Branca ou "preta ou parda" (categoria única)
- _Rendimento per capita:_ Faixa salarial medida em salários mínimos, nos intervalos $(0,\frac12),(\frac12,1),(1,2)(2,3),(3,5)$ e $(5,\infty)$
 
 Segue o código implementado:
```python
class Pessoa:
    def __init__(self, tipo_grad,rede_ensino,modalidade,dif_frequencia,sexo,cor,rendimento_percapita):
        self.tipo_grad = tipo_grad 
        self.rede_ensino = rede_ensino 
        self.modalidade = modalidade 
        self.dif_frequencia = dif_frequencia 
        self.sexo = sexo 
        self.cor = cor 
        self.rendimento_percapita = rendimento_percapita 
```
### Classe População
A classe Populacao do arquivo [Populacao.py](https://github.com/josearthursouza/ProjetoVerao2019/blob/master/Populacao.py) é a que vai realizar todo o trabalho de geração de populações "arbitrárias", amostragem e geração dos atributos.

Inicia-se com o seguinte código base:
```python
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
```
São importados: a bilbioteca _random_ e o arquivo Pessoa.py, para que seja possível usar a classe já criada.
Depois disso, a classe população é definida com apenas um parâmetro de entrada: o __tamanho__ da população que se deseja gerar, que é pré-definido como 1000.
Ocorre também a geração da lista de __indivíduos__ que é onde conterão as pessoas. Para isso, a classe Pessoa é chamada, e são passados à ela, todos os 7 atributos necessários, que são gerados chamando as funções geradoras, que serão descritas a seguir, dentro da própria classe.

Depois, gera-se uma função amostra, que utiliza o método _sample_ da biblioteca random. É dado para este método a lista de indivíduos e um número N que é o tamanho da amostra; é feito então um "sorteio" aleatório de N elementos entre a lista dada, que retorna uma nova lista de tamanho N, que será a nossa amostra.

#### Funções geradoras de atributos
Para gerar uma população onde os seus atributos seguem razoavelmente os dados oficiais da PNAD, um ideia muito simples foi implementada:
Utilizamos os valores absolutos de cada categoria, "jogamos uma moeda", ou seja, geramos um número aleatório entre zero e o total absoluto da PNAD, e vemos em qual faixa o valor se encaixa.
Por exemlo, no caso de sexo, cujas duas únicas categorias são homem e mulher, usamos o total absoluto de $7288$, e dentre estes segunda os dados oficiais, $3118$ eram homens e $4170$ eram mulheres. A "moeda" vai então de zero ao total de $7288$, e se for menor que $3118$ o sexo da pessoa gerada será homem, se for maior, será mulher.

Essa abordagem garante que, criando uma população razoavelmente grande, a proporção de sexos esteja compatível com os dados reais. Entretanto, temos que incluir no cálculo o coeficiente de variação, que nada mais é do que a média sobre o desvio padrão da dispersão dos dados, que mostra o "_erro_" da distribuição dos dados. Este valor na planilha do IBGE é dado em percentual.
No caso do sexo, o "_cv_" (coeficiente de variação) dos homens é de $1.7\%$, ou seja, a proporção de homens é $3118$ de $7288$ com uma "_margem de erro_" de $1,7\%$ para mais ou para menos.
Com isso definimos uma variável __j__ que a cada chamada da função irá gerar um número aleatório pertencente ao intervalo $[3118-\frac{17}{100}\cdot3118,3118+\frac{17}{100}\cdot3118)$. Esse número __j__ é que será utilizado como parâmetro de divisão quando a moeda for jogada, e não o valor $3118$ cravado; e isso implementa na simulação o coeficiente de variação dos dados.
```python
    def sexo():
        cv1 = (1.7)/100
        j = random.uniform(3118*(1-cv1), 3118*(1+cv1))
        m = random.uniform(0, 7288)
        if m <= j:
            return 'Homem'
        else:
            return 'Mulher'
```






