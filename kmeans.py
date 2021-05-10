#PASSO 1 - utilitários - calcular media

#multiplica um vetor por um escalar
def scalar_multiply (escalar, vetor):
    return [escalar * i for i in vetor]

#soma n vetores
def vector_sum (vetores):
    resultado = vetores[0]
    for vetor in vetores[1:]:
        resultado = [resultado[i] + vetor[i] for i in range(len(vetor))]
    return resultado

# calcula a média de n vetores
def vector_mean (vetores):
    return scalar_multiply ( 1 / len(vetores), vector_sum(vetores))

#PASSO 2 - utilitários - calcular distancia entre vetores

#produto escalar
def dot (v, w):
    return sum(v_i * w_i for v_i, w_i in zip(v, w))

# subtração de vetores
def vector_subtract (v, w):
    return [v_i - w_i for v_i, w_i in zip (v, w)]
#soma dos quadrados
def sum_of_squares (v):
    return dot (v, v)

#distância ao quadrado
def squared_distance (v, w):
    return sum_of_squares (vector_subtract(v, w))


#PASSO3 - Implementação do algoritmo KMeans)
class KMeans:
    def __init__ (self, k, means = None):
        self.k = k
        self.means = means
    def classify (self, ponto):
        return min (range (self.k), key = lambda i: squared_distance(ponto, self.means[i]))
    def train (self, pontos):
        #escolha de k elementos
        #self.means = random.sample (pontos, self.k)
        #nenhuma atribuição, para começar
        assignments = None
        while True:
            #associa cada instância a um inteiro 0 <= i < k
            new_assignments = list(map (self.classify, pontos))
            #se não houver mudança, termina
            if new_assignments == assignments:
                return
            #atribuição atual se torna a nova
            assignments = new_assignments
            self.grupoMeans = []
            #cálculo das novas médias
            for i in range (self.k):
                #pontos associados ao agrupamento i
                #note que pontos e assignments estão na ordem
                #por exemplo pontos = [1, 2, 3] e assignments = [1, 2, 2]
                #indicam que a primeira instância está no grupo 1 e as demais
                # no grupo 2
                i_points = [p for p, a in zip (pontos, assignments) if a == i ]

                self.grupoMeans.append(i_points)
                # tem alguém nesse grupo?
                if i_points:
                    self.means[i] = vector_mean (i_points)                    

#PASSO 4 - testando algoritmo
def test_k_means ():
    dados = [[1], [2], [3], [6], [7], [10], [11]]
    kmeans = KMeans(3, [[1], [3], [11]])
    kmeans.train(dados)
    print (kmeans.means)
    print (kmeans.grupoMeans)

test_k_means()

# 1. A implementação do algoritmo K-Means vista em aula somente permite que as médias finais sejam   visualizadas.   Ajuste   o   algoritmo   para   que   todos   os   elementos   de   cada   grupo   sejam armazenados em uma estrutura de dados apropriada. Adicione uma função à classe que exibe a coleção.
