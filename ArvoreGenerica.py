# Definição da classe 'No' que representa um nó de uma árvore genérica
class No:
    # Inicializa o nó com um valor e uma lista vazia de filhos
    def __init__(self, valor):
        self.valor = valor  # O valor do nó
        self.filhos = []  # Lista de filhos do nó
    
    # Método para adicionar um filho ao nó
    def adicionar_filho(self, filho):
        self.filhos.append(filho)  # Adiciona o filho à lista de filhos
    
    # Método para representar o nó como uma string (apenas o valor do nó)
    def __str__(self):
        return str(self.valor)
    
    # Método para imprimir a árvore a partir de um nó
    def imprimir_arvore(self, prefixo="", eh_ultimo=True):
        # Imprime o nó atual com seu prefixo adequado
        print(prefixo + ("└── " if eh_ultimo else "├── ") + str(self.valor))
        # Atualiza o prefixo para a próxima linha de acordo se o nó é o último filho ou não
        prefixo += "    " if eh_ultimo else "│   "
        # Chama recursivamente para cada filho do nó, marcando o último filho
        for i, filho in enumerate(self.filhos):
            filho.imprimir_arvore(prefixo, i == len(self.filhos) - 1)

# Função recursiva para contar o número de nós na árvore
def contar_nos_recursivo(raiz):
    if not raiz:  # Caso base: Se o nó não existir, retorna 0
        return 0
    # Retorna 1 (para o nó atual) + a soma do número de nós nos filhos
    return 1 + sum(contar_nos_recursivo(filho) for filho in raiz.filhos)

# Função não-recursiva para contar o número de nós na árvore
def contar_nos_naoRecursivo(raiz):
    if not raiz:  # Caso base: Se o nó não existir, retorna 0
        return 0
    contador = 0  # Contador para armazenar o número de nós
    fila = [raiz]  # Fila para armazenar os nós a serem visitados
    while fila:  # Enquanto houver nós na fila
        no_atual = fila.pop(0)  # Remove o nó da fila
        contador += 1  # Incrementa o contador
        fila.extend(no_atual.filhos)  # Adiciona os filhos do nó atual à fila
    return contador  # Retorna o número total de nós

# Função recursiva para somar os valores de todos os nós na árvore
def somar_nos_recursivo(raiz):
    if not raiz:  # Caso base: Se o nó não existir, retorna 0
        return 0
    # Retorna o valor do nó atual + a soma dos valores dos filhos
    return raiz.valor + sum(somar_nos_recursivo(filho) for filho in raiz.filhos)

# Função não-recursiva para somar os valores de todos os nós na árvore
def somar_nos_naoRecursivo(raiz):
    if not raiz:  # Caso base: Se o nó não existir, retorna 0
        return 0
    soma = 0  # Variável para armazenar a soma dos valores dos nós
    pilha = [raiz]  # Pilha para armazenar os nós a serem visitados
    while pilha:  # Enquanto houver nós na pilha
        no_atual = pilha.pop()  # Remove o nó da pilha
        soma += no_atual.valor  # Adiciona o valor do nó atual à soma
        pilha.extend(no_atual.filhos)  # Adiciona os filhos do nó atual à pilha
    return soma  # Retorna a soma total dos valores dos nós

# Função recursiva para calcular a profundidade da árvore
def profundidade_recursivo(raiz):
    if not raiz:  # Caso base: Se o nó não existir, a profundidade é 0
        return 0
    # Retorna 1 (para o nó atual) + a profundidade máxima dos filhos
    return 1 + max((profundidade_recursivo(filho) for filho in raiz.filhos), default=0)

# Função não-recursiva para calcular a profundidade da árvore
def profundidade_naoRecursivo(raiz):
    if not raiz:  # Caso base: Se o nó não existir, a profundidade é 0
        return 0
    max_profundidade = 0  # Inicializa a profundidade máxima como 0
    pilha = [(raiz, 1)]  # Pilha para armazenar os nós e suas profundidades atuais
    while pilha:  # Enquanto houver nós na pilha
        no_atual, profundidade_atual = pilha.pop()  # Remove o nó e sua profundidade da pilha
        max_profundidade = max(max_profundidade, profundidade_atual)  # Atualiza a profundidade máxima
        for filho in no_atual.filhos:  # Para cada filho do nó atual
            pilha.append((filho, profundidade_atual + 1))  # Adiciona o filho à pilha com profundidade incrementada
    return max_profundidade  # Retorna a profundidade máxima

# Criação da árvore de exemplo
raiz = No(10)  # Cria o nó raiz com valor 10
filho1 = No(5)  # Cria um filho com valor 5
filho2 = No(20)  # Cria um filho com valor 20
filho3 = No(15)  # Cria um filho com valor 15

# Adiciona os filhos à raiz
raiz.adicionar_filho(filho1)
raiz.adicionar_filho(filho2)
filho2.adicionar_filho(filho3)

# Imprime a estrutura da árvore
print("Estrutura da árvore:")
raiz.imprimir_arvore()  # Chama o método para imprimir a árvore

# Chama e imprime as funções para contar os nós, somar valores e calcular profundidade
print("\nNúmero de nós(Recursivo):", contar_nos_recursivo(raiz))  # Chama a função recursiva para contar os nós
print("Número de nós(Não Recursivo):", contar_nos_naoRecursivo(raiz))  # Chama a função não-recursiva para contar os nós
print("Soma dos valores dos nós(Recursivo):", somar_nos_recursivo(raiz))  # Chama a função recursiva para somar os valores
print("Soma dos valores dos nós(Não Recursivo):", somar_nos_naoRecursivo(raiz))  # Chama a função não-recursiva para somar os valores
print("Profundidade da árvore(Recursivo):", profundidade_recursivo(raiz))  # Chama a função recursiva para calcular a profundidade
print("Profundidade da árvore(Não recursivo):", profundidade_naoRecursivo(raiz))  # Chama a função não-recursiva para calcular a profundidade
