import Pessoa
import Populacao as pop

# Brasil=Populacao
# Brasil.individuos()

p1 = pop.Populacao(100)
print(p1.individuos[0].rendimento_percapita)

print(p1.amostra(10)[0])
