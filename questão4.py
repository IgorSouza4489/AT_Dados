import random
import time

isbn_sorted = list(range(1, 100001))
target_isbn = random.choice(isbn_sorted)

#https://www.freecodecamp.org/portuguese/news/pesquisa-binaria-em-python-como-escrever-o-algoritmo-de-pesquisa-binaria-e-exemplos/
def busca_binaria(lista, alvo):
    inicio = 0
    fim = len(lista) - 1
    i = 0
    while inicio <= fim:
        i += 1
        meio = (inicio + fim) // 2
        if lista[meio] == alvo:
            return i  
        elif lista[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1
    return i 

def busca_linear(lista, alvo):
    i = 0
    for item in lista:
        i += 1
        if item == alvo:
            return i  
    return i  


def executar():
    start_binaria = time.time()
    i_binaria = busca_binaria(isbn_sorted, target_isbn)
    tempo_binaria = time.time() - start_binaria

    start_linear = time.time()
    i_linear = busca_linear(isbn_sorted, target_isbn)
    tempo_linear = time.time() - start_linear

    # Resultados
    print(f"ISBN binário encontrado: {target_isbn}")
    print(f"Número de iterações binário: {i_binaria}")
    print(f"Tempo de execução binário: {tempo_binaria:.6f} segundos")

    print(f"ISBN linear encontrado: {target_isbn}")
    print(f"Número de iterações linear: {i_linear}")
    print(f"Tempo de execução linear:{tempo_linear:.6f} segundos")
