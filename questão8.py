#https://www.geeksforgeeks.org/python-program-for-selection-sort/
def selection_sort(jogadores):
    for i in range(len(jogadores)):
        maior_indice = i
        for j in range(i + 1, len(jogadores)):
            if jogadores[j]['pontuacao'] > jogadores[maior_indice]['pontuacao']:
                maior_indice = j
        jogadores[i], jogadores[maior_indice] = jogadores[maior_indice], jogadores[i]
    return jogadores

def executar():
    jogadores = [
        {'nome': 'Jogador1', 'pontuacao': 100},
        {'nome': 'Jogador2', 'pontuacao': 200},
        {'nome': 'Jogador3', 'pontuacao': 150},
        {'nome': 'Jogador4', 'pontuacao': 50},
    ]

    jogadores_ordenados = selection_sort(jogadores)

    for jogador in jogadores_ordenados:
        print(f"{jogador['nome']}: {jogador['pontuacao']}")
