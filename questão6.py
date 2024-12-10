import random
import time

def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        trocou = False
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]  # Troca
                trocou = True
        if not trocou:
            break
    return lista

def testar_bubble_sort(tamanho_lista):
    lista_precos = [random.randint(1, 10000) for _ in range(tamanho_lista)]
    inciio = time.time()
    bubble_sort(lista_precos)
    fim = time.time()
    return fim - inciio

def executar():
    tempo_1k = testar_bubble_sort(1000)
    print(f"mil elementos: {tempo_1k:.6f} segundos")
    tempo_10k = testar_bubble_sort(10000)
    print(f"10 mil elementos: {tempo_10k:.6f} segundos")
